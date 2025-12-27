import os
import subprocess
import sys

# Nom du projet
PROJECT_NAME = "bibmath_rdc"

# Contenu des fichiers
files_content = {
    "requirements.txt": """Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Login==0.6.3
Flask-WTF==1.2.1
email_validator==2.1.0.post1
Werkzeug==3.0.1
""",
    "config.py": """import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-tres-difficile-a-deviner-pour-bibmath-rdc'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Base de données SQLite
    DB_PATH = os.path.join(BASE_DIR, 'data', 'bibmath.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
""",
    "models.py": """from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='student')
    points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resumes = db.relationship('Resume', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Resume(db.Model):
    __tablename__ = 'resume'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    content_latex = db.Column(db.Text, nullable=False)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
""",
    "app.py": """import os
from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db, User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Création du dossier data si inexistant
    os.makedirs(os.path.join(app.config['BASE_DIR'], 'data'), exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    from routes.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
""",
    "routes/__init__.py": "",
    "routes/main.py": """from flask import Blueprint, render_template, request
from models import Resume

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/resumes')
def resumes():
    subject_filter = request.args.get('subject')
    query = Resume.query.filter_by(is_published=True)
    if subject_filter:
        query = query.filter_by(subject=subject_filter)
    resumes_list = query.order_by(Resume.created_at.desc()).all()
    return render_template('resumes.html', resumes=resumes_list)
""",
    "static/css/style.css": """/* CSS moderne pour Bibmath RDC */
:root {
    --primary-color: #1a1a2e;
    --accent-color: #162447;
    --btn-color: #e43f5a;
}

body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f5f5f5;
    color: #333;
}

.navbar {
    background-color: var(--primary-color) !important;
}

.navbar .nav-link {
    color: #fff !important;
    font-weight: 500;
}

.card-resume {
    transition: transform 0.3s, box-shadow 0.3s;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.card-resume:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

.btn-primary {
    background-color: var(--btn-color);
    border-color: var(--btn-color);
}

.btn-primary:hover {
    background-color: #d73650;
    border-color: #d73650;
}
""",
    "static/js/main.js": """// JS basique pour interactions
document.addEventListener('DOMContentLoaded', function() {
    console.log('Bibmath RDC ready!');
    // Exemple : ajouter plus tard filtres ou animations
});
""",
    "seed_db.py": """from app import create_app
from models import db, User, Resume

app = create_app()

def seed():
    with app.app_context():
        print("🌱 Nettoyage de la base de données...")
        db.drop_all()
        db.create_all()

        admin = User(username="Admin", email="admin@bibmath.cd", role="admin")
        admin.set_password("admin123")
        prof = User(username="Prof.Kambale", email="prof@bibmath.cd", role="teacher")
        prof.set_password("prof123")
        etudiant = User(username="Etudiant", email="student@bibmath.cd", role="student")
        etudiant.set_password("student123")

        db.session.add_all([admin, prof, etudiant])
        db.session.commit()

        resumes_data = [
            {"title": "Identités Remarquables", "subject": "maths", "level": "debutant", "content": r"Soient $a, b \\in \\mathbb{R}$. On a : $$(a+b)^2 = a^2 + 2ab + b^2$$ $$(a-b)^2 = a^2 - 2ab + b^2$$ $$a^2 - b^2 = (a-b)(a+b)$$"},
            {"title": "Lois de Newton", "subject": "physique", "level": "intermediaire", "content": r"1. **Principe d'inertie** : $\\sum \\vec{F} = \\vec{0} \\iff \\vec{v} = \\vec{constante}$ \\\\ 2. **Dynamique** : $\\sum \\vec{F}_{ext} = m \\cdot \\vec{a}$"},
            {"title": "Intégration par parties", "subject": "maths", "level": "avance", "content": r"Si $u$ et $v$ sont dérivables sur $[a, b]$ : $$\\int_a^b u(x)v'(x) \\,dx = [u(x)v(x)]_a^b - \\int_a^b u'(x)v(x) \\,dx$$"}
        ]

        for r in resumes_data:
            resume = Resume(title=r["title"], subject=r["subject"], level=r["level"], content_latex=r["content"], author=prof)
            db.session.add(resume)

        db.session.commit()
        print("✅ Base de données initialisée avec succès (SQLite) !")

if __name__ == "__main__":
    seed()
"""
}

def create_project():
    # Création du dossier racine
    if not os.path.exists(PROJECT_NAME):
        os.makedirs(PROJECT_NAME)
        print(f"📁 Dossier '{PROJECT_NAME}' créé.")
    else:
        print(f"⚠️ Le dossier '{PROJECT_NAME}' existe déjà.")

    # Création des fichiers
    for filepath, content in files_content.items():
        full_path = os.path.join(PROJECT_NAME, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"📄 Fichier créé : {filepath}")

    # Création des dossiers vides supplémentaires
    empty_dirs = ["static/css", "static/js", "static/img", "data"]
    for d in empty_dirs:
        os.makedirs(os.path.join(PROJECT_NAME, d), exist_ok=True)
        print(f"📁 Dossier créé : {d}")

    # Création d'un environnement virtuel
    venv_path = os.path.join(PROJECT_NAME, "venv")
    if not os.path.exists(venv_path):
        subprocess.run([sys.executable, "-m", "venv", venv_path])
        print(f"🔧 Environnement virtuel créé : {venv_path}")

    # Installation des dépendances
    pip_executable = os.path.join(venv_path, "Scripts", "pip") if os.name == "nt" else os.path.join(venv_path, "bin", "pip")
    subprocess.run([pip_executable, "install", "-r", os.path.join(PROJECT_NAME, "requirements.txt")])
    print("📦 Dépendances installées avec succès.")

    print("\n✅ PROJET AMÉLIORÉ GÉNÉRÉ AVEC SUCCÈS !")
    print("\n--- INSTRUCTIONS ---")
    if os.name == "nt":
        print(f"1. cd {PROJECT_NAME}")
        print("2. venv\\Scripts\\activate")
    else:
        print(f"1. cd {PROJECT_NAME}")
        print("2. source venv/bin/activate")
    print("3. python seed_db.py")
    print("4. python app.py")

if __name__ == "__main__":
    create_project()
