from src.utils.constants import PROMPT


def get_prompt(category: str, email_content: str) -> str:
    """
    Gera o prompt baseado na categoria e conteúdo do email.
    """
    if category == "Produtivo":
        return PROMPT["PRODUTIVO"]
    else:
        return PROMPT["IMPRODUTIVO"]
