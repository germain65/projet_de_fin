import pytest
import tempfile
import os
from bibmath_rdc.app import create_app
from bibmath_rdc.models import db, User

class TestConfig:
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def auth(client):
    class AuthActions:
        def login(self, email='test@bibmath.cd', password='test123'):
            return client.post('/auth/login', data={'email': email, 'password': password})
        
        def logout(self):
            return client.get('/auth/logout')
    
    return AuthActions()