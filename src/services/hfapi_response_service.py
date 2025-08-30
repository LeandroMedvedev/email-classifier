import os

import requests
from dotenv import load_dotenv

load_dotenv()


class HFAPIResponseService:
    def __init__(self):
        self.api_url = (
            "https://api-inference.huggingface.co/models/google/flan-t5-large"
        )
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_TOKEN')}"}

    def generate_response(self, category: str, email_content: str) -> str:
        if category == "Produtivo":
            prompt = (
                f"Escreva uma resposta profissional para este e-mail:\n\n"
                f"{email_content}"
            )
        else:
            prompt = (
                f"Escreva uma resposta curta, amigável e educada:\n\n{email_content}"
            )

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 150, "temperature": 0.7},
        }

        response_obj = requests.post(self.api_url, headers=self.headers, json=payload)
        response = response_obj.json()

        try:
            return response[0]["generated_text"].strip()
        except Exception:
            return "Não foi possível gerar a resposta no momento."
