FROM python:3.10-slim

# Ustawienie katalogu roboczego
WORKDIR /backend

# Skopiowanie pliku requirements.txt
COPY requirements.txt ./

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiowanie całego kodu aplikacji
COPY . .

# Domyślna komenda uruchamiania serwera
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]