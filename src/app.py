from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.controllers import email_controller
from src.utils.text_preprocessor import TextPreprocessor


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Lifespan handler: executa antes de aceitar requests.
    Carrega o modelo de NLP uma vez por processo.
    """
    # Pré-carrega o modelo (cada processo do Uvicorn fará isso)
    TextPreprocessor._get_nlp()
    try:
        yield
    finally:
        # Se precisar liberar recursos
        pass


app = FastAPI(title="Email Classifier API", lifespan=lifespan)

# Configurar templates e static
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# Registrar rotas
app.include_router(email_controller.router, prefix="/emails", tags=["Emails"])


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
