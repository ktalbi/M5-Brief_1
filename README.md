# M5 – Brief 1

## Description
Ce projet est un **backend Python** structuré de manière modulaire, intégrant :
- une logique métier claire
- des tests unitaires avec `pytest`
- une intégration continue GitHub Actions
- un **déploiement via Docker**

---

## Architecture du projet

```
M5-Brief_1/
├── backend/
│   ├── modules/
│   │   ├── __init__.py
│   │   └── calcul.py
│   ├── tests/
│   │   └── test_calcul.py
│   ├── requirements.txt
│   ├── main.py
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── test.yml
├── docker-compose.yml
└── README.md
```

---

## Logique métier

### Module `calcul`
Fichier : `backend/modules/calcul.py`

```python
def calcul_carre(x: int | float) -> int | float:
    return x * x
```

---

## Tests unitaires

Fichier : `backend/tests/test_calcul.py`

```python
from modules.calcul import calcul_carre

def test_calcul_carre():
    assert calcul_carre(4) == 16
```

Lancement local :
```bash
cd backend
export PYTHONPATH=$PWD
pytest
```

---

## Routes (exemple API)

Si une API FastAPI est utilisée :

| Méthode | Route      | Description |
|-------|-----------|-------------|
| GET   | /health   | Healthcheck |
| POST  | /carre    | Calcul du carré |

---

## Lancement en local (sans Docker)

```bash
git clone https://github.com/ktalbi/M5-Brief_1.git
cd M5-Brief_1/backend

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export PYTHONPATH=$PWD
python main.py
```

---

## Déploiement avec Docker

### Dockerfile (backend/Dockerfile)
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["python", "main.py"]
```

### docker-compose.yml
```yaml
version: "3.9"

services:
  backend:
    build: ./backend
    container_name: m5_backend
    ports:
      - "8000:8000"
```

### Lancer l’application
```bash
docker-compose up --build
```

Arrêt :
```bash
docker-compose down
```

---

## Intégration Continue (CI)

Le workflow GitHub Actions :
- installe Python
- installe les dépendances
- exécute les tests `pytest`
- bloque le merge si échec

Fichier : `.github/workflows/test.yml`


