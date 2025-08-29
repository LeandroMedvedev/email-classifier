from transformers import pipeline


class EmailClassifier:
    def __init__(
        self,
        model_name: str = ("distilbert-base-uncased-finetuned-sst-2-english"),
    ):
        """
        Inicializa o classificador de e-mails usando Hugging Face pipeline.
        """
        self.classifier = pipeline(
            "text-classification", model=model_name, device=-1
        )  # device=-1 para forçar uso da CPU

    def classify(self, email_text: str) -> str:
        """
        Classifica um e-mail como Produtivo ou Improdutivo.
        """
        result = self.classifier(email_text[:512])[
            0
        ]  # limitando o tamanho do texto para 512 tokens
        label = result["label"]

        # Adaptando saída do modelo para nossas categorias
        if label == "POSITIVE":
            return "Produtivo"
        else:
            return "Improdutivo"
