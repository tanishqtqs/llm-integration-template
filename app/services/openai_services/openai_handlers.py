from openai import OpenAI
from .openai_constants import GPT_DEFAULT_MODEL
from .openai_schemas import DefaultResponseFormat
from config import OPENAI_API_KEY

class OpenAIService:
    def __init__(self):
        self.gpt = OpenAI(api_key=OPENAI_API_KEY)
        
    def api_call_openai(self, prompt_input, model=GPT_DEFAULT_MODEL, response_format=DefaultResponseFormat):
        try:
            prompt = prompt_input

            completion = self.gpt.beta.chat.completions.parse(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format=response_format,
            )

            themes = completion.choices[0].message.parsed
            return themes.model_dump()
        except Exception as e:
            raise Exception(e)
