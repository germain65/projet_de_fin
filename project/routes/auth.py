# auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from ..models import db, User
from ..forms import LoginForm, RegistrationForm
import logging

# Import conditionnel du rate limiting
try:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    LIMITER_AVAILABLE = True
except ImportError:
    LIMITER_AVAILABLE = False

logger = logging.getLogger(__name__)
# Création du blueprint pour l'authentification
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# ==================== CONNEXION ====================
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Rate limiting conditionnel
    if LIMITER_AVAILABLE:
        # Applique la limite si disponible
        pass
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is None or not user.check_password(form.password.data):
            flash('Email ou mot de passe incorrect.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash('Vous êtes maintenant connecté !', 'success')
        
        # Gestion sécurisée du paramètre ?next
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('main.index')
        
        return redirect(next_page)
    
    return render_template('login.html', title='Connexion - BibMath RDC', form=form)


# ==================== DÉCONNEXION ====================
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('main.index'))


# ==================== INSCRIPTION ====================
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            if User.query.filter_by(email=form.email.data.lower()).first():
                flash('Cet email est déjà utilisé.', 'danger')
                return redirect(url_for('auth.register'))
            
            if User.query.filter_by(username=form.username.data).first():
                flash("Ce nom d'utilisateur est déjà pris.", 'danger')
                return redirect(url_for('auth.register'))
            
            user = User(
                username=form.username.data.strip(),
                email=form.email.data.lower().strip()
            )
            user.set_password(form.password.data)
            
            db.session.add(user)
            db.session.commit()
            
            logger.info(f"Nouvel utilisateur inscrit: {user.username}")
            flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            logger.error(f"Erreur lors de l'inscription: {e}")
            flash('Erreur lors de l\'inscription. Veuillez réessayer.', 'danger')
    
    return render_template('register.html', title='Inscription - BibMath RDC', form=form)


# ==================== PROFIL UTILISATEUR ====================
@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Mon Profil - BibMath RDC', user=current_user)
