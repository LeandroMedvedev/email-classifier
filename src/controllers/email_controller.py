from fastapi import APIRouter, Form, UploadFile

from src.services.nlp_service import EmailClassifier

router = APIRouter()
classifier = EmailClassifier()


@router.post("/classify")
async def classify_email(file: UploadFile = None, text: str = Form(None)):
    """
    Endpoint para classificar e-mails enviados por upload (.txt/.pdf) ou texto direto.
    """
    content = ""

    if file:
        # Leitura simples (tratamento de PDF será feito depois)
        content = (await file.read()).decode("utf-8")
    elif text:
        content = text
    else:
        return {"error": "No input provided."}

    category = classifier.classify(content)

    return {
        "category": category,
        "suggested_response": (
            f"E-mail identificado como {category}. "
            "Resposta automática será sugerida na próxima etapa."
        ),
    }
