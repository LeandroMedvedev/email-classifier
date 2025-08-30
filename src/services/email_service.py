from src.services.hfapi_response_service import HFAPIResponseService
from src.services.local_response_service import LocalResponseService
from src.services.nlp_service import EmailClassifier


class EmailService:
    def __init__(self, use_hf_api: bool = False):
        self.classifier = EmailClassifier()
        self.response_service = (
            LocalResponseService() if not use_hf_api else HFAPIResponseService()
        )

    def classify_email(self, classification_text: str, generation_text: str) -> dict:
        """
        classification_text: texto pré-processado para classificação
        generation_text: texto quase cru para geração de resposta
        """
        # Classificação
        category = self.classifier.classify(classification_text)

        # Geração de resposta
        response = self.response_service.generate_response(category, generation_text)

        return {"category": category, "response": response}
