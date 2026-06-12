PROMPT = """
You are a nutrition expert.

Analyze this meal:

{meal}

Estimate:

1. Calories (kcal)
2. Protein (g)
3. Carbohydrates (g)
4. Fat (g)
5. Health score out of 10
6. Three suggestions
7. Two better alternatives

Return ONLY a JSON object.

Do not include explanations.
Do not include markdown.
Do not include ```json.

Use exactly this format:

{{
    "calories": 0,
    "protein": 0,
    "carbs": 0,
    "fat": 0,
    "health_score": 0,
    "suggestions": [
        "Suggestion 1",
        "Suggestion 2",
        "Suggestion 3"
    ],
    "alternatives": [
        "Alternative 1",
        "Alternative 2"
    ]
}}
"""