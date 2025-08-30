from transformers import pipeline

from src.utils.get_prompt import get_prompt


class LocalResponseService:
    def __init__(self, model_name: str = "google/flan-t5-base"):
        self.generator = pipeline("text2text-generation", model=model_name, device=-1)

    def generate_response(self, category: str, email_content: str) -> str:
        """
        Gera uma resposta automática para o e-mail com base na categoria.
        """
        prompt = get_prompt(category, email_content)
        response = self.generator(prompt, max_new_tokens=200)
        return response[0]["generated_text"].strip()
