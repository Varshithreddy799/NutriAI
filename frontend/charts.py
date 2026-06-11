import plotly.express as px


def nutrient_chart(result):

    labels = ["Protein", "Carbs", "Fat"]

    values = [
        result["protein"],
        result["carbs"],
        result["fat"]
    ]

    fig = px.pie(
        values=values,
        names=labels,
        title="Macronutrient Distribution"
    )

    return fig