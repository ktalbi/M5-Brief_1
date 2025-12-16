import streamlit as st
import requests
from loguru import logger

API_URL = "http://backend:8000"

st.title("Calcul du carré")

valeur = st.number_input("Entrez un entier", step=1)

if st.button("Calculer"):
    logger.info(f"Valeur envoyée : {valeur}")
    response = requests.post(
        f"{API_URL}/calcul",
        json={"valeur": int(valeur)}
    )

    if response.status_code == 200:
        resultat = response.json()["resultat"]
        st.success(f"Résultat : {resultat}")
    else:
        st.error("Erreur API")

