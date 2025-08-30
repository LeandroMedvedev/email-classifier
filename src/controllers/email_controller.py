from fastapi import APIRouter, Form, UploadFile

from src.services.email_service import EmailService
from src.utils.file_reader import FileReader
from src.utils.text_preprocessor import TextPreprocessor

router = APIRouter()


@router.post("/classify")
async def upload_email(file: UploadFile = None, text: str = Form(None)):
    """
    Endpoint para classificar e-mails enviados por upload (.txt/.pdf) ou texto direto.
    """
    content = ""

    if file:
        if file.filename.endswith(".txt"):
            content = FileReader.read_txt(file.file)
        elif file.filename.endswith(".pdf"):
            content = FileReader.read_pdf(file.file)
        else:
            return {
                "error": (
                    "Formato de arquivo não suportado. Por favor, use .txt ou .pdf."
                )
            }
    elif text:
        content = text
    else:
        return {"error": "Nenhum conteúdo enviado."}

    preprocessed_text = TextPreprocessor.preprocess(content)

    service = EmailService()
    result = service.classify_email(preprocessed_text)

    return result
