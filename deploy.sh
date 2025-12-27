#!/bin/bash

echo "🚀 Déploiement de BibMath RDC"

# Installation des dépendances
echo "📦 Installation des dépendances..."
pip install -r bibmath_rdc/requirements.txt

# Initialisation de la base de données
echo "🗄️ Initialisation de la base de données..."
python init_db.py

# Tests
echo "🧪 Exécution des tests..."
pytest

# Démarrage de l'application
echo "🌟 Démarrage de l'application..."
python run.py