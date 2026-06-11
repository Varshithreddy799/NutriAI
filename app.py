import streamlit as st
from backend.analyzer import analyze_meal
from frontend.charts import nutrient_chart

st.set_page_config(
    page_title="NutriAI",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 NutriAI - AI Food Nutrition Analyzer")

meal = st.text_area(
    "Enter your meal",
    "2 idlis, 1 banana, 1 glass milk"
)

provider = st.radio(
    "Choose AI Provider",
    [
        "Ollama (Local AI)",
        "Gemini API (BYOK)"
    ]
)

api_key = None

if provider == "Gemini API (BYOK)":
    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

if st.button("Analyze Meal"):

    result = analyze_meal(
        meal,
        provider,
        api_key
    )

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

    st.header("Health Score")

    score = result["health_score"]

    st.progress(score / 10)

    if score >= 8:
        st.success(f"⭐⭐⭐⭐⭐ {score}/10 Healthy Meal")
    elif score >= 5:
        st.warning(f"⭐⭐⭐⭐ {score}/10 Moderate Meal")
    else:
        st.error(f"⭐⭐ {score}/10 Unhealthy Meal")

    st.header("Suggestions")

    for tip in result["suggestions"]:
        st.write("✔", tip)

    st.header("Better Alternatives")

    for alt in result["alternatives"]:
        st.write("🥗", alt)

    st.plotly_chart(
        nutrient_chart(result),
        use_container_width=True
    )