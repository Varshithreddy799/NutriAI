from backend.gemini_model import analyze_with_gemini


def analyze_meal(
        meal,
        provider,
        api_key=None
):

    if not api_key:

        raise ValueError(
            "Please enter your Gemini API key."
        )

    return analyze_with_gemini(
        meal,
        api_key
    )