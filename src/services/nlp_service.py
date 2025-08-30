from transformers import pipeline


class EmailClassifier:
    def __init__(self, model_name: str = "facebook/bart-large-mnli"):
        """
        Inicializa o classificador de e-mails usando Hugging Face pipeline (zero-shot).
        """
        self.classifier = pipeline(
            "zero-shot-classification", model=model_name, device=-1
        )  # "device=-1" para forçar uso da CPU

    def classify(self, email_text: str) -> str:
        """
        Classifica um e-mail como Produtivo ou Improdutivo.
        """
        labels = ["Produtivo", "Improdutivo"]
        result = self.classifier(email_text, candidate_labels=labels)
        return result["labels"][0]  # retorna a categoria mais provável
