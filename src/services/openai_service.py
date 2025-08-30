import os

from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Carregar chave da API do OpenAI a partir do .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class OpenAIService:
    @staticmethod
    def generate_response(category: str, email_content: str) -> str:
        """
        Gera uma resposta inteligente baseada na categoria e no conteúdo do e-mail.
        """
        print(email_content)
        if category == "Produtivo":
            prompt = (
                f"Responda a este e-mail de modo profissional e eficaz: {email_content}"
            )
        else:
            prompt = (
                f"Responda a este e-mail de modo amigável e casual: {email_content}"
            )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,  # Para respostas mais criativas
        )

        return response.choices[0].message.content.strip()
