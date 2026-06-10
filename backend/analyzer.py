import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from backend.prompt import PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_meal(meal):
    try:
        prompt = PROMPT.format(meal=meal)

        response = model.generate_content(prompt)

        if not hasattr(response, "text") or response.text is None:
            return json.dumps({
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "health_score": 0,
                "suggestions": [
                    "Gemini returned an empty response."
                ],
                "alternatives": [
                    "Please try again after a few seconds."
                ]
            })

        return response.text

    except Exception as e:
        return json.dumps({
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0,
            "health_score": 0,
            "suggestions": [
                f"Error: {str(e)}"
            ],
            "alternatives": [
                "Please try again later."
            ]
        })