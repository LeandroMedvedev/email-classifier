from src.services.hfapi_response_service import HFAPIResponseService
from src.services.nlp_service import EmailClassifier
from src.services.response_service import ResponseService


class EmailService:
    def __init__(self, use_hf_api: bool = False):
        self.classifier = EmailClassifier()
        self.response_service = (
            ResponseService() if not use_hf_api else HFAPIResponseService()
        )

    def classify_email(self, email_text: str) -> dict:
        category = self.classifier.classify(email_text)

        # Gerar resposta inteligente usando Hugging Face API ou modelo local
        response = self.response_service.generate_response(category, email_text)

        return {"category": category, "response": response}
