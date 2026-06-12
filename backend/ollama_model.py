import ollama
import json
import re

from backend.prompt import PROMPT


def analyze_with_ollama(meal):

    prompt = PROMPT.format(
        meal=meal
    )

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response["message"]["content"]

    print("\nRAW OLLAMA RESPONSE:\n")
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

    text = text.strip()

    # Extract JSON object
    match = re.search(
        r'\{.*\}',
        text,
        re.DOTALL
    )

    if not match:

        raise ValueError(
            "Ollama did not return valid JSON."
        )

    json_text = match.group()

    print("\nEXTRACTED JSON:\n")
    print(json_text)

    return json.loads(
        json_text
    )