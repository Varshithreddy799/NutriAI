PROMPT = """
You are a nutrition expert.

Analyze the following meal:

{meal}

Provide:

1. Total calories (kcal)
2. Protein (grams)
3. Carbohydrates (grams)
4. Fat (grams)
5. Health score out of 10
6. Three suggestions for improvement
7. Two healthier alternatives

Return ONLY JSON in the following format:

{{
    "calories": 0,
    "protein": 0,
    "carbs": 0,
    "fat": 0,
    "health_score": 0,
    "suggestions": [],
    "alternatives": []
}}
"""