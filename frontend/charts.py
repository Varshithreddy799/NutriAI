import plotly.express as px


def nutrient_chart(result):

    protein = float(result["protein"])
    carbs = float(result["carbs"])
    fat = float(result["fat"])

    labels = [
        "Protein",
        "Carbs",
        "Fat"
    ]

    values = [
        protein,
        carbs,
        fat
    ]

    fig = px.pie(
        names=labels,
        values=values,
        title="Macronutrient Distribution"
    )

    return fig