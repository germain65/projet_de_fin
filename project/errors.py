"""
Module de gestion des erreurs pour BibMath RDC
"""

import logging
from flask import render_template, request, jsonify
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)

def register_error_handlers(app):
    """Enregistre les gestionnaires d'erreurs pour l'application"""
    
    @app.errorhandler(400)
    def bad_request(error):
        logger.warning(f"Requête invalide: {request.url} - {error}")
        if request.is_json:
            return jsonify({'error': 'Requête invalide'}), 400
        return render_template('errors/400.html'), 400
    
    @app.errorhandler(403)
    def forbidden(error):
        logger.warning(f"Accès interdit: {request.url} - {error}")
        if request.is_json:
            return jsonify({'error': 'Accès interdit'}), 403
        return render_template('errors/403.html'), 403
    
    @app.errorhandler(404)
    def not_found(error):
        logger.info(f"Page non trouvée: {request.url}")
        if request.is_json:
            return jsonify({'error': 'Ressource non trouvée'}), 404
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Erreur interne: {request.url} - {error}")
        if request.is_json:
            return jsonify({'error': 'Erreur interne du serveur'}), 500
        return render_template('500.html'), 500
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        """Gestionnaire d'erreur générique"""
        if isinstance(error, HTTPException):
            return error
        
        logger.error(f"Erreur non gérée: {request.url} - {error}", exc_info=True)
        if request.is_json:
            return jsonify({'error': 'Une erreur inattendue s\'est produite'}), 500
        return render_template('500.html'), 500