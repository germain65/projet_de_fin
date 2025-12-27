from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import Resume, Exercise, Chapter, Category, Quiz, Question, db
from ..forms import QuizForm, QuestionForm
from sqlalchemy.orm import joinedload
import logging

# Import conditionnel du cache
try:
    from ..app import cache
    CACHE_AVAILABLE = True
except ImportError:
    CACHE_AVAILABLE = False
    cache = None

logger = logging.getLogger(__name__)
main_bp = Blueprint('main', __name__)

# -------------------------------
# Page d'accueil
# -------------------------------
@main_bp.route('/')
def index():
    return render_template('index.html')


# -------------------------------
# Pages de résumés
# -------------------------------
@main_bp.route('/resumes')
def resumes():
    if CACHE_AVAILABLE and cache:
        @cache.cached(timeout=300)
        def _cached_resumes():
            subject_filter = request.args.get('subject')
            query = Resume.query.filter_by(is_published=True)
            if subject_filter:
                query = query.filter_by(subject=subject_filter)
            return query.order_by(Resume.created_at.desc()).all()
        resumes_list = _cached_resumes()
    else:
        subject_filter = request.args.get('subject')
        query = Resume.query.filter_by(is_published=True)
        if subject_filter:
            query = query.filter_by(subject=subject_filter)
        resumes_list = query.order_by(Resume.created_at.desc()).all()
    
    subject_filter = request.args.get('subject')
    return render_template('resumes.html', resumes=resumes_list, selected_subject=subject_filter)


@main_bp.route('/resume/<int:resume_id>')
def resume_detail(resume_id):
    if CACHE_AVAILABLE and cache:
        @cache.cached(timeout=600)
        def _cached_resume(resume_id):
            return Resume.query.get_or_404(resume_id)
        resume = _cached_resume(resume_id)
    else:
        resume = Resume.query.get_or_404(resume_id)
    return render_template('resume_detail.html', resume=resume)


# -------------------------------
# Pages d'exercices
# -------------------------------
@main_bp.route('/exercises')
def exercises():
    subject_filter = request.args.get('subject')

    query = Chapter.query  # ← Plus de .options(joinedload(...))

    if subject_filter:
        query = query.filter(Chapter.subject == subject_filter)

    chapters_list = query.order_by(Chapter.name).all()

    # Chargement manuel des catégories si besoin
    for chapter in chapters_list:
        chapter.categories  # déclenche le lazy loading

    return render_template('exercises.html', chapters=chapters_list, selected_subject=subject_filter)

@main_bp.route('/category/<int:category_id>')
def category_detail(category_id):
    category = Category.query.get_or_404(category_id)
    exercises = category.exercises.order_by(Exercise.difficulty).all()
    return render_template('category_detail.html', category=category, exercises=exercises)

# -------------------------------
# Page de contact
# -------------------------------
@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Ici, tu pourrais ajouter l'envoi de mail
        flash('Votre message a bien été envoyé ! Nous vous répondrons dès que possible.')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')


# -------------------------------
# Pages de quiz
# -------------------------------
@main_bp.route('/quizzes')
def quizzes():
    subject_filter = request.args.get('subject')
    level_filter = request.args.get('level')
    query = Quiz.query
    if subject_filter:
        query = query.filter_by(subject=subject_filter)
    if level_filter:
        query = query.filter_by(level=level_filter)
    quizzes_list = query.order_by(Quiz.created_at.desc()).all()
    return render_template('quiz_list.html', quizzes=quizzes_list, selected_subject=subject_filter, selected_level=level_filter)

@main_bp.route('/quiz/create', methods=['GET', 'POST'])
@login_required
def create_quiz():
    form = QuizForm()
    if form.validate_on_submit():
        try:
            quiz = Quiz(title=form.title.data, subject=form.subject.data, level=form.level.data, author_id=current_user.id)
            db.session.add(quiz)
            db.session.commit()
            flash('Quiz créé avec succès !')
            logger.info(f"Quiz créé: {quiz.title} par {current_user.username}")
            return redirect(url_for('main.quiz_detail', quiz_id=quiz.id))
        except Exception as e:
            db.session.rollback()
            logger.error(f"Erreur lors de la création du quiz: {e}")
            flash('Erreur lors de la création du quiz.')
    return render_template('create_quiz.html', form=form)

@main_bp.route('/quiz/<int:quiz_id>')
def quiz_detail(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions.all()
    return render_template('quiz_detail.html', quiz=quiz, questions=questions)

@main_bp.route('/quiz/<int:quiz_id>/add_question', methods=['GET', 'POST'])
@login_required
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if quiz.author_id != current_user.id:
        flash('Vous n\'avez pas la permission d\'ajouter des questions à ce quiz.')
        return redirect(url_for('main.quiz_detail', quiz_id=quiz_id))
    form = QuestionForm()
    if form.validate_on_submit():
        options = form.options.data.split('\n')
        question = Question(quiz_id=quiz_id, question_text=form.question_text.data, options=options, correct_answer=form.correct_answer.data, explanation=form.explanation.data)
        db.session.add(question)
        db.session.commit()
        flash('Question ajoutée avec succès !')
        return redirect(url_for('main.quiz_detail', quiz_id=quiz_id))
    return render_template('add_question.html', form=form, quiz=quiz)

@main_bp.route('/quiz/<int:quiz_id>/take', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        score = 0
        total = len(questions)
        for question in questions:
            user_answer = request.form.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        flash(f'Votre score : {score}/{total}')
        return redirect(url_for('main.quiz_detail', quiz_id=quiz_id))
    return render_template('take_quiz.html', quiz=quiz, questions=questions)


# -------------------------------
# Gestion des erreurs
# -------------------------------
@main_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@main_bp.app_errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
