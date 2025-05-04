# Używamy oficjalnego obrazu Pythona
FROM python:3.12-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki projektu
COPY . .

# Instalujemy zależności
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn joblib

# Udostępniamy port
EXPOSE 8000

# Komenda uruchamiająca aplikację
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]