import streamlit as st


# ----------------------------
# Health Score
# ----------------------------
def show_health_score(score):

    st.header("Health Score")

    st.progress(score / 10)

    if score >= 8:
        st.success(
            f"⭐⭐⭐⭐⭐ {score}/10 Healthy Meal"
        )

    elif score >= 5:
        st.warning(
            f"⭐⭐⭐⭐ {score}/10 Moderate Meal"
        )

    else:
        st.error(
            f"⭐⭐ {score}/10 Needs Improvement"
        )


# ----------------------------
# Suggestions
# ----------------------------
def show_suggestions(suggestions):

    st.header("Suggestions")

    if not suggestions:
        st.info(
            "No suggestions available."
        )

        return

    for item in suggestions:

        st.write(
            "✔",
            item
        )


# ----------------------------
# Better Alternatives
# ----------------------------
def show_alternatives(alternatives):

    st.header(
        "Better Alternatives"
    )

    if not alternatives:

        st.info(
            "No alternatives available."
        )

        return

    for item in alternatives:

        st.write(
            "🥗",
            item
        )


# ----------------------------
# Final Verdict
# ----------------------------
def show_final_verdict(score):

    st.header(
        "Final Verdict"
    )

    if score >= 8:

        st.success(
            "🟢 Healthy Meal ⭐⭐⭐⭐⭐"
        )

    elif score >= 5:

        st.warning(
            "🟡 Moderate Meal ⭐⭐⭐⭐"
        )

    else:

        st.error(
            "🔴 Needs Improvement ⭐⭐"
        )