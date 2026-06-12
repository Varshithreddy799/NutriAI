import google.generativeai as genai
import json
import re

from backend.prompt import PROMPT


def analyze_with_gemini(meal, api_key):

    if not api_key:
        raise ValueError(
            "Please enter your Gemini API key."
        )

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = PROMPT.format(
        meal=meal
    )

    response = model.generate_content(
        prompt
    )

    text = response.text.strip()

    print("\nRAW GEMINI RESPONSE:\n")
    print(text)

    # Remove markdown blocks
    text = text.replace(
        "```json",
        ""
    )

    text = text.replace(
        "```",
        ""
    )

    # Extract JSON object
    match = re.search(
        r'\{.*\}',
        text,
        re.DOTALL
    )

    if not match:

        raise ValueError(
            "Gemini did not return valid JSON."
        )

    json_text = match.group()

    print("\nEXTRACTED JSON:\n")
    print(json_text)

    return json.loads(
        json_text
    )