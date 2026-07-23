import ollama

from app.config.settings import settings


class OllamaClient:

    def generate(self, prompt: str):

        response = ollama.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]