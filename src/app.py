from fastapi import FastAPI

from src.controllers import email_controller

app = FastAPI(title="Email Classifier API")

# Registrar rotas
app.include_router(email_controller.router, prefix="/emails", tags=["Emails"])


@app.get("/")
async def root():
    return {"message": "Email Classifier API is running!"}
