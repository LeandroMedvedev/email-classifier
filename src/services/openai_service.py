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
                f"Você é um assistente profissional de e-mails em português. "
                f"Leia o e-mail abaixo e escreva uma resposta clara, educada e "
                f"objetiva em nome da equipe da empresa, como se estivesse "
                f"respondendo ao cliente. "
                f"Não copie o conteúdo do e-mail, apenas responda de forma "
                f"apropriada.\n\n"
                f"E-mail recebido:\n{email_content}\n\n"
                f"Resposta:"
            )
        else:
            prompt = (
                f"Você é um assistente simpático que responde e-mails em português. "
                f"Escreva uma resposta curta, amigável e educada para o e-mail abaixo. "
                f"Não repita o texto do e-mail, apenas responda de forma "
                f"apropriada.\n\n"
                f"E-mail recebido:\n{email_content}\n\n"
                f"Resposta:"
            )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,  # Para respostas mais criativas
        )

        return response.choices[0].message.content.strip()
