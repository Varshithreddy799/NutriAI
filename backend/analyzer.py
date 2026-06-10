import os
import google.generativeai as genai
from dotenv import load_dotenv
from backend.prompt import PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_meal(meal):
    try:
        prompt = PROMPT.format(meal=meal)

        print("Sending request to Gemini...")

        response = model.generate_content(prompt)

        print("Response received!")

        # Make sure Gemini actually returned text
        if not hasattr(response, "text") or response.text is None:
            return """
            {
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fat": 0,
                "health_score": 0,
                "suggestions": [
                    "Gemini returned an empty response. Please try again."
                ],
                "alternatives": [
                    "Try again after a few seconds."
                ]
            }
            """

        return response.text

    except Exception as e:
        return f"""
        {{
            "calories": 0,
            "protein": 0,
            "carbs": 0,
            "fat": 0,
            "health_score": 0,
            "suggestions": [
                "Error: {str(e)}"
            ],
            "alternatives": [
                "Please try again later."
            ]
        }}
        """