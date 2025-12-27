#!/usr/bin/env python3
"""
Point d'entrée principal pour l'application BibMath RDC
"""

import os
import sys

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bibmath_rdc.app import create_app

if __name__ == '__main__':
    # Configuration sécurisée pour la production
    os.environ.setdefault('FLASK_ENV', 'development')
    app = create_app()
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)