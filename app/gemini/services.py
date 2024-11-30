import google.generativeai as genai

from ..config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)


def send_message(
    message: str,
    introduction_prompt: str,
) -> str:

    model = genai.GenerativeModel(
        model_name=settings.GEMINI_MODEL,
        system_instruction=introduction_prompt,
    )

    generation_config_dict = {
        'max_output_tokens': 20,
        'temperature': 1.0,
    }

    response = model.generate_content(
        message,
        generation_config=genai.types.GenerationConfig(
            **generation_config_dict
        )
    )

    return response.text
