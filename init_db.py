#!/usr/bin/env python3
"""
Script d'initialisation de la base de données BibMath RDC
"""


import os
import sys

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from project.seed_db import seed

if __name__ == '__main__':
    print("🌱 Initialisation de la base de données BibMath RDC...")
    seed()
    print("✅ Base de données initialisée avec succès !")
