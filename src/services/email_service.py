from src.services.nlp_service import EmailClassifier
from src.services.openai_service import OpenAIService


class EmailService:
    def __init__(self):
        self.classifier = EmailClassifier()
        self.openai_service = OpenAIService()

    def classify_email(self, email_text: str) -> dict:
        category = self.classifier.classify(email_text)

        # Gerar resposta inteligente usando OpenAI
        response = self.openai_service.generate_response(category, email_text)

        return {"category": category, "response": response}
