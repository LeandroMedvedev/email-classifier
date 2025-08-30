from transformers import pipeline


class ResponseService:
    def __init__(self, model_name: str = "google/flan-t5-base"):
        self.generator = pipeline("text2text-generation", model=model_name, device=-1)

    def generate_response(self, category: str, email_content: str) -> str:
        """
        Gera uma resposta automática para o e-mail com base na categoria.
        """
        if category == "Produtivo":
            prompt = (
                f"Escreva uma resposta profissional para este e-mail:\n\n"
                f"{email_content}"
            )
        else:
            prompt = (
                f"Escreva uma resposta curta, amigável e educada:\n\n{email_content}"
            )

        response = self.generator(prompt)

        return response[0]["generated_text"].strip()
