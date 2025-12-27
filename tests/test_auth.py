import pytest
from bibmath_rdc.models import User, db

def test_register(client, app):
    response = client.get('/auth/register')
    assert response.status_code == 200
    
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'test@bibmath.cd',
        'password': 'test123',
        'password2': 'test123'
    })
    assert response.status_code == 302

def test_login_logout(client, app):
    with app.app_context():
        user = User(username='testuser', email='test@bibmath.cd')
        user.set_password('test123')
        db.session.add(user)
        db.session.commit()
    
    response = client.post('/auth/login', data={
        'email': 'test@bibmath.cd',
        'password': 'test123'
    })
    assert response.status_code == 302
    
    response = client.get('/auth/logout')
    assert response.status_code == 302

def test_login_required(client):
    response = client.get('/auth/profile')
    assert response.status_code == 302