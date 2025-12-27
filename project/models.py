# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# ===================================================================
# Modèle Utilisateur
# ===================================================================
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='student')  # student, teacher, admin
    points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations
    resumes = db.relationship('Resume', backref='author', lazy='dynamic', cascade="all, delete-orphan")
    exercises = db.relationship('Exercise', backref='author', lazy='dynamic', cascade="all, delete-orphan")
    quizzes = db.relationship('Quiz', backref='author', lazy='dynamic', cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username} - {self.role}>'

# ===================================================================
# Modèle Résumé de cours (indépendant)
# ===================================================================
class Resume(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(50), nullable=False)  # maths, physique, chimie
    level = db.Column(db.String(50), nullable=False)   # debutant, intermediaire, avance
    content_latex = db.Column(db.Text, nullable=False)
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Clé étrangère vers l'auteur
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Resume {self.title}>'

# ===================================================================
# Modèle Chapitre (ex: "Mathématiques", "Physique")
# ===================================================================
class Chapter(db.Model):
    __tablename__ = 'chapters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)     # ex: "Mathématiques"
    subject = db.Column(db.String(50), nullable=False)  # maths, physique, chimie
    description = db.Column(db.Text, nullable=True)

    # Relation : un chapitre a plusieurs catégories
    categories = db.relationship('Category', backref='chapter', lazy='select', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Chapter {self.name} - {self.subject}>'

# ===================================================================
# Modèle Catégorie (ex: "Identités Remarquables", "Lois de Newton")
# ===================================================================
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Clé étrangère vers le chapitre
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)

    # Relation : une catégorie a plusieurs exercices
    exercises = db.relationship('Exercise', backref='category', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Category {self.name}>'

# ===================================================================
# Modèle Exercice
# ===================================================================
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)    # debutant, intermediaire, avance
    difficulty = db.Column(db.Integer, default=1)      # 1 à 5
    statement_latex = db.Column(db.Text, nullable=False)
    solution_latex = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Clés étrangères
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Exercise {self.title} - {self.difficulty}★>'

# ===================================================================
# Modèle Quiz (QCM)
# ===================================================================
class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)    # debutant, intermediaire, avance
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Clé étrangère vers l'auteur
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relation : un quiz a plusieurs questions
    questions = db.relationship('Question', backref='quiz', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Quiz {self.title}>'

# ===================================================================
# Modèle Question (pour QCM)
# ===================================================================
class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON, nullable=False)  # Liste des choix (ex: ["A", "B", "C", "D"])
    correct_answer = db.Column(db.String(200), nullable=False)  # La réponse correcte
    explanation = db.Column(db.Text, nullable=True)

    # Clé étrangère vers le quiz
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)

    def __repr__(self):
        return f'<Question {self.question_text[:50]}...>'
