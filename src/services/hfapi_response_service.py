import os

import requests
from dotenv import load_dotenv

from src.utils.get_prompt import get_prompt

load_dotenv()


class HFAPIResponseService:
    def __init__(self):
        self.api_url = (
            "https://api-inference.huggingface.co/models/google/flan-t5-large"
        )
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}

    def generate_response(self, category: str, email_content: str) -> str:
        """
        Gera uma resposta automática para o e-mail usando Hugging Face Inference API.
        """
        prompt = get_prompt(category, email_content)
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200, "temperature": 0.7, "top_p": 0.9},
        }
        response_obj = requests.post(self.api_url, headers=self.headers, json=payload)
        response = response_obj.json()
        try:
            return response[0]["generated_text"].strip()
        except Exception:
            return "Não foi possível gerar a resposta no momento."
