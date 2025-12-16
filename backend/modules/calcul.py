from loguru import logger

def calcul_carre(x: int) -> int:
    logger.info(f"Calcul du carré de {x}")
    return x * x
