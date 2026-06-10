import streamlit as st
import plotly.express as px
import json

from backend.analyzer import analyze_meal

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

    try:
        # Get response from Gemini
        response = analyze_meal(meal)

        # Display raw response for debugging
        st.write("Gemini Response:")
        st.write(response)

        # Remove markdown formatting
        response = response.replace("```json", "").replace("```", "").strip()

        # Convert JSON string to dictionary
        result = json.loads(response)

        # Nutrition Facts
        st.subheader("🍽️ Nutrition Facts")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Calories", f"{result['calories']} kcal")
            st.metric("Protein", f"{result['protein']} g")

        with col2:
            st.metric("Carbohydrates", f"{result['carbs']} g")
            st.metric("Fat", f"{result['fat']} g")

        # Health Score
        st.subheader("❤️ Health Score")

        score = result["health_score"]

        st.progress(score / 10)

        if score >= 8:
            st.success(f"⭐⭐⭐⭐ {score}/10 Healthy Meal")
        elif score >= 5:
            st.warning(f"⭐⭐⭐ {score}/10 Moderate Meal")
        else:
            st.error(f"⭐⭐ {score}/10 Needs Improvement")

        # Suggestions
        st.subheader("💡 Suggestions")

        for suggestion in result["suggestions"]:
            st.write("✔", suggestion)

        # Better Alternatives
        st.subheader("🥗 Better Alternatives")

        for alt in result["alternatives"]:
            st.write("👉", alt)

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

        if score >= 8:
            st.success("⭐⭐⭐⭐ Healthy Meal")
        elif score >= 5:
            st.warning("⭐⭐⭐ Moderate Meal")
        else:
            st.error("⭐⭐ Needs Improvement")

        # Meal Summary
        st.subheader("📝 Meal Summary")

        st.info(
            f"This meal provides approximately {result['calories']} kcal with "
            f"{result['protein']} g protein, {result['carbs']} g carbohydrates "
            f"and {result['fat']} g fat."
        )

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.success(
    "🏆 Team Tech_Titans | NutriAI – AI Food Nutrition Analyzer\n\n"
    "⚡ Powered by Gemini AI"
)