import google.generativeai as genai
import json
from .gemini_constants import GEMINI_DEFAULT_MODEL
from .gemini_schemas import generation_config
from config import GEMINI_API_KEY

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)

    def api_call_gemini(self, prompt_input, model=GEMINI_DEFAULT_MODEL, response_format=generation_config):
        try:
            model_instance = genai.GenerativeModel(
                model_name=model,
                generation_config=response_format,
            )
            prompt = prompt_input
            response = model_instance.generate_content(prompt)

            results = response.to_dict()

            res = results["candidates"][0]["content"]["parts"][0]["text"]
            json_data = json.loads(res)

            return json_data
        except Exception as e:
            raise Exception(f"Error during Gemini API call: {str(e)}")
