from typing import Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel

from src.services.email_service import EmailService
from src.utils.text_preprocessor import TextPreprocessor

router = APIRouter(prefix="/emails", tags=["emails"])
service = EmailService()


class EmailIn(BaseModel):
    email: str


def _read_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore")


def _read_pdf(file_bytes: bytes) -> str:
    import io

    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(file_bytes))
    pages = []
    for p in reader.pages:
        try:
            pages.append(p.extract_text() or "")
        except Exception:
            pages.append("")
    return "\n".join(pages).strip()


@router.post("/classify")
async def classify_email(
    file: Optional[UploadFile] = File(None),
    email: Optional[str] = Form(None),
):
    text_content: Optional[str] = None

    if file:
        filename = (file.filename or "").lower()
        content = await file.read()

        if filename.endswith(".txt"):
            text_content = _read_txt(content)
        elif filename.endswith(".pdf"):
            try:
                text_content = _read_pdf(content)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Falha ao ler PDF: {e}")
        else:
            raise HTTPException(
                status_code=400, detail="Formato não suportado. Envie .txt ou .pdf."
            )
    elif email:
        text_content = email.strip()

    if not text_content:
        raise HTTPException(
            status_code=400, detail="Nenhum conteúdo encontrado (texto vazio?)."
        )

    # Pré-processamento para classificação
    classification_text = TextPreprocessor.preprocess_for_classification(text_content)

    # Passa o texto cru (quase sem alterações) para geração
    generation_text = TextPreprocessor.preprocess_for_generation(text_content)

    result = service.classify_email(
        classification_text=classification_text, generation_text=generation_text
    )
    return result
