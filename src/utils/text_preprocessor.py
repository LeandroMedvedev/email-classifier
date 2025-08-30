import re
import string
from typing import Optional

import spacy
from spacy.language import Language


class TextPreprocessor:
    _nlp: Optional[Language] = None

    @classmethod
    def _get_nlp(cls) -> Language:
        """
        Carrega o modelo pt_core_news_sm uma vez (lazy load).
        """
        if cls._nlp is None:
            try:
                cls._nlp = spacy.load("pt_core_news_sm")
            except OSError:
                # Fallback leve caso o modelo não esteja instalado
                cls._nlp = spacy.blank("pt")
        return cls._nlp

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Limpeza leve: minúsculas, remoção de URLs, pontuação e espaços extras.
        """
        text = text.lower()
        text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
        text = text.translate(str.maketrans("", "", string.punctuation))
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def lemmatize(cls, text: str) -> str:
        """
        Lematização com spaCy (útil apenas para classificação).
        """
        nlp = cls._get_nlp()
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        return " ".join(tokens)

    @classmethod
    def preprocess_for_classification(cls, text: str) -> str:
        """
        Pré-processamento recomendado para classificação.
        """
        cleaned = cls.clean_text(text)
        lemmatized = cls.lemmatize(cleaned)
        return lemmatized

    @staticmethod
    def preprocess_for_generation(text: str) -> str:
        """
        Pré-processamento mínimo para geração de respostas.
        Mantém o texto quase cru, apenas removendo ruídos visuais.
        """
        return re.sub(r"\s+", " ", text).strip()
