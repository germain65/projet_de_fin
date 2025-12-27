# =========================
# IMPORTS STANDARD PYTHON
# =========================

import os
# os est utilisé pour :
# - manipuler les chemins de fichiers de manière portable
# - créer des dossiers (ici le dossier "data")
# - lire des variables d’environnement (FLASK_ENV)

import logging
# logging permet de :
# - tracer ce que fait l’application (info, warning, erreur)
# - diagnostiquer les bugs en production ou en développement


# =========================
# IMPORTS FLASK & EXTENSIONS
# =========================

from flask import Flask
# Flask est la classe principale qui représente l’application web

from flask_login import LoginManager
# Flask-Login gère :
# - l’authentification des utilisateurs
# - la session utilisateur
# - la protection des routes nécessitant une connexion


# =========================
# IMPORTS INTERNES AU PROJET
# =========================

from .config import Config
# Config contient toute la configuration centralisée :
# - SECRET_KEY
# - URI de la base de données
# - BASE_DIR, etc.

from .models import db, User
# db : instance SQLAlchemy partagée dans tout le projet
# User : modèle représentant un utilisateur (nécessaire pour Flask-Login)


# =========================
# CONFIGURATION DU LOGGING
# =========================

logging.basicConfig(
    level=logging.INFO,  # Niveau minimal des messages affichés
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Ce format permet :
# - une lecture claire
# - un suivi chronologique précis

logger = logging.getLogger(__name__)
# logger spécifique à ce module (bonne pratique)


# =========================
# CONFIGURATION FLASK-LOGIN
# =========================

login_manager = LoginManager()
# Instance centrale de Flask-Login

login_manager.login_view = 'auth.login'
# Nom de la route vers laquelle un utilisateur non connecté
# sera redirigé s’il tente d’accéder à une route protégée


@login_manager.user_loader
def load_user(user_id):
    """
    Fonction obligatoire pour Flask-Login.

    Elle permet de recharger un utilisateur à partir de son ID
    stocké dans la session.
    """
    return db.session.get(User, int(user_id))


# =========================
# FACTORY DE L’APPLICATION
# =========================

def create_app(config_class=Config):
    """
    Application Factory :
    - permet de créer plusieurs instances de l’app
    - facilite les tests
    - évite les effets de bord globaux
    """

    app = Flask(__name__)
    # __name__ permet à Flask de savoir
    # où chercher les ressources (templates, static)

    app.config.from_object(config_class)
    # Charge toute la configuration depuis la classe Config


    # =========================
    # CRÉATION DES DOSSIERS NÉCESSAIRES
    # =========================

    data_dir = os.path.join(app.config['BASE_DIR'], 'data')
    os.makedirs(data_dir, exist_ok=True)
    # Crée le dossier "data" s’il n’existe pas
    # exist_ok=True évite une exception si le dossier existe déjà


    # =========================
    # INITIALISATION DES EXTENSIONS
    # =========================

    db.init_app(app)
    # Lie SQLAlchemy à l’application Flask

    login_manager.init_app(app)
    # Active Flask-Login sur l’application


    # =========================
    # ENREGISTREMENT DES BLUEPRINTS
    # =========================

    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    # Blueprint principal (pages publiques, accueil, etc.)

    try:
        from .routes.auth import auth_bp
        app.register_blueprint(auth_bp)
        logger.info("Blueprint auth enregistré avec succès")
    except ImportError as e:
        # Permet à l’application de fonctionner
        # même si le module auth n’est pas encore implémenté
        logger.warning(f"Blueprint auth non trouvé : {e}")


    # =========================
    # CRÉATION DES TABLES
    # =========================

    with app.app_context():
        # Le contexte applicatif est nécessaire
        # pour accéder à la configuration et à la base de données

        try:
            db.create_all()
            logger.info("Tables de base de données créées avec succès")
        except Exception as e:
            logger.error(f"Erreur lors de la création des tables : {e}")


    return app


# =========================
# POINT D’ENTRÉE DU SCRIPT
# =========================

if __name__ == '__main__':
    app = create_app()

    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    # Le mode debug :
    # - affiche les erreurs détaillées
    # - recharge automatiquement le serveur

    app.run(
        debug=debug_mode,
        host='127.0.0.1',
        port=5000
    )
