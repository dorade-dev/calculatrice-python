# Image de base Python
FROM python:3.9-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier le code dans le conteneur
COPY calculatrice.py .

# Commande à exécuter
CMD ["python3", "calculatrice.py"]
