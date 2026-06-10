import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="NutriAI",
    page_icon="🥗",
    layout="wide"
)

# Title
st.title("🥗 NutriAI – AI Food Nutrition Analyzer")

# Input section
meal = st.text_area(
    "Enter your meal",
    placeholder="Example: 2 idlis, 1 banana, 1 glass milk"
)

# Analyze button
analyze = st.button("Analyze Meal")

if analyze:

    result = {
        "calories": 420,
        "protein": 16,
        "carbs": 55,
        "fat": 9,
        "health_score": 8,
        "suggestions": [
            "Good breakfast choice",
            "Add nuts for healthy fats",
            "Increase protein slightly"
        ],
        "alternatives": [
            "Add boiled eggs for more protein",
            "Add nuts for healthy fats"
        ]
    }

    # Display results
    st.subheader("Nutrition Facts")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Calories", f"{result['calories']} kcal")
        st.metric("Protein", f"{result['protein']} g")

    with col2:
        st.metric("Carbohydrates", f"{result['carbs']} g")
        st.metric("Fat", f"{result['fat']} g")

    # Health score
    st.subheader("Health Score")
    st.progress(result["health_score"]/10)
    st.success(f"⭐⭐⭐⭐ {result['health_score']}/10 Healthy Meal")

    # Suggestions
    st.subheader("Suggestions")

    for suggestion in result["suggestions"]:
        st.write("✔", suggestion)

    # Better Alternatives
    st.subheader("Better Alternatives")

    for alt in result["alternatives"]:
        st.write("🥗", alt)

    # Pie Chart
    st.subheader("📊 Macronutrient Distribution")

    labels = ["Protein", "Carbohydrates", "Fat"]

    values = [
        result["protein"],
        result["carbs"],
        result["fat"]
    ]

    fig = px.pie(
        values=values,
        names=labels,
        title="Macronutrient Breakdown"
    )

    st.plotly_chart(fig)
    # Final Verdict
    st.subheader("🎯 Final Verdict")

    score = result["health_score"]

    if score >= 8:
        st.success("⭐⭐⭐⭐ Healthy Meal")
    elif score >= 5:
        st.warning("⭐⭐⭐ Moderate Meal")
    else:
        st.error("⭐⭐ Needs Improvement")

# Meal Summary
    st.subheader("📝 Meal Summary") 

    st.info(
        "Balanced meal with moderate carbohydrates and good protein content. "
        "Consider adding healthy fats and slightly increasing protein."
    )