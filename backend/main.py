from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from modules.calcul import calcul_carre

app = FastAPI(title="API Calcul")

logger.add("logs/app.log", rotation="5 MB")
logger.info("Logger initialisé")

class CalculRequest(BaseModel):
    valeur: int

class CalculResponse(BaseModel):
    resultat: int

@app.get("/")
def root():
    logger.info("Route / appelée")
    return {"message": "API opérationnelle"}

@app.get("/health")
def health():
    logger.info("Health check OK")
    return {"status": "ok"}

@app.post("/calcul", response_model=CalculResponse)
def calcul(data: CalculRequest):
    resultat = calcul_carre(data.valeur)
    return {"resultat": resultat}

