from backend.locales.en import translations as en
from backend.locales.te import translations as te
from backend.locales.pa import translations as pa

import streamlit as st

from backend.analyzer import analyze_meal

from frontend.charts import nutrient_chart

from frontend.components import (
    show_health_score,
    show_suggestions,
    show_alternatives,
    show_final_verdict
)

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="NutriAI",
    page_icon="🥗",
    layout="wide"
)

# ----------------------------
# Language Selection
# ----------------------------
lang = st.sidebar.selectbox(
    "🌐 Language",
    [
        "English",
        "తెలుగు",
        "ਪੰਜਾਬੀ"
    ]
)

if lang == "English":
    T = en

elif lang == "తెలుగు":
    T = te

else:
    T = pa

# ----------------------------
# Title
# ----------------------------
st.title(T["title"])

# ----------------------------
# Meal Input
# ----------------------------
meal = st.text_area(
    T["meal_input"]
)

# ----------------------------
# AI Provider
# ----------------------------
provider = st.radio(
    "Choose AI Provider",
    [
        "Gemini API (BYOK)",
        "Ollama (Local AI)"
    ]
)

api_key = None

if provider == "Gemini API (BYOK)":

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

# ----------------------------
# Analyze Button
# ----------------------------
if st.button(T["analyze_button"]):

    if meal.strip() == "":

        st.warning("Please enter a meal.")

    elif provider == "Gemini API (BYOK)" and not api_key:

        st.error("Please enter your Gemini API key.")

    else:

        with st.spinner("Analyzing meal..."):

            try:

                result = analyze_meal(
                    meal,
                    provider,
                    api_key
                )

                # ----------------------------
                # Nutrition Facts
                # ----------------------------
                st.header("Nutrition Facts")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Calories",
                        f"{result['calories']} kcal"
                    )

                    st.metric(
                        "Protein",
                        f"{result['protein']} g"
                    )

                with col2:

                    st.metric(
                        "Carbs",
                        f"{result['carbs']} g"
                    )

                    st.metric(
                        "Fat",
                        f"{result['fat']} g"
                    )

                # ----------------------------
                # Health Score
                # ----------------------------
                show_health_score(
                    result["health_score"]
                )

                # ----------------------------
                # Suggestions
                # ----------------------------
                show_suggestions(
                    result["suggestions"]
                )

                # ----------------------------
                # Alternatives
                # ----------------------------
                show_alternatives(
                    result["alternatives"]
                )

                # ----------------------------
                # Pie Chart
                # ----------------------------
                st.header(
                    "Macronutrient Distribution"
                )

                st.plotly_chart(
                    nutrient_chart(result),
                    use_container_width=True
                )

                # ----------------------------
                # Final Verdict
                # ----------------------------
                show_final_verdict(
                    result["health_score"]
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )