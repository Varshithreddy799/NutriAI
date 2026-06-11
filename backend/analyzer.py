import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from backend.prompt import PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")



def analyze_meal(meal, provider, api_key=None):

    return {
        "calories": 420,
        "protein": 16,
        "carbs": 55,
        "fat": 9,
        "health_score": 8,
        "suggestions": [
            "Good breakfast choice",
            "Add some nuts for healthy fats",
            "Increase protein slightly"
        ],
        "alternatives": [
            "Add boiled eggs",
            "Add sprouts"
        ]
    }