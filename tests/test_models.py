import pytest
from bibmath_rdc.models import User, Quiz, Question

def test_user_password_hashing():
    user = User(username='test', email='test@bibmath.cd')
    user.set_password('test123')
    assert user.password_hash != 'test123'
    assert user.check_password('test123')
    assert not user.check_password('wrong')

def test_user_repr():
    user = User(username='test', email='test@bibmath.cd')
    assert repr(user) == '<User test>'

def test_quiz_creation(app):
    with app.app_context():
        quiz = Quiz(title='Test Quiz', description='Test Description')
        assert quiz.title == 'Test Quiz'
        assert quiz.description == 'Test Description'