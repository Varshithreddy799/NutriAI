import os
import google.generativeai as genai
from dotenv import load_dotenv
from backend.prompt import PROMPT

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key loaded:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_meal(meal):
    try:
        prompt = PROMPT.format(meal=meal)

        print("Sending request to Gemini...")

        response = model.generate_content(prompt)

        print("Response received!")

        return response.text

    except Exception as e:
        print("ERROR:", e)
        return None