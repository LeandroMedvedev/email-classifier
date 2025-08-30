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
        # Minúsculas
        text = text.lower()
        # Remove URLs
        text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
        # Remove pontuação
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Remove múltiplos espaços
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def lemmatize(cls, text: str) -> str:
        nlp = cls._get_nlp()
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if not token.is_stop]
        return " ".join(tokens)

    @classmethod
    def preprocess(cls, text: str) -> str:
        cleaned = cls.clean_text(text)
        lemmatized = cls.lemmatize(cleaned)
        # cleaned = TextPreprocessor.clean_text(text)
        # lemmatized = TextPreprocessor.lemmatize(cleaned)
        return lemmatized
