# 📚 BibMath RDC - Guide d'Installation et d'Utilisation

## 🚀 Installation Rapide

### Prérequis
- Python 3.8+ installé
- pip (gestionnaire de paquets Python)

### 1. Installation de Base

```bash
# Cloner ou télécharger le projet
cd projet_de_fin

# Installer les dépendances essentielles
pip install -r bibmath_rdc/requirements.txt

# Initialiser la base de données
python init_db.py

# Lancer l'application
python run.py
```

### 2. Accès à l'Application
Ouvrir http://127.0.0.1:5000 dans votre navigateur

## 👥 Comptes de Test

| Rôle | Email | Mot de passe |
|------|-------|--------------|
| Admin | admin@bibmath.cd | admin123 |
| Professeur | kambale@bibmath.cd | prof123 |
| Étudiant | etudiant1@bibmath.cd | student123 |

## 🔧 Extensions Optionnelles

### Sécurité Avancée (Rate Limiting + CAPTCHA)
```bash
pip install Flask-Limiter==3.5.0 Flask-ReCaptcha==0.4.2
```

### Performance (Cache)
```bash
pip install Flask-Caching==2.1.0
```

### Tests
```bash
pip install pytest==7.4.3 pytest-flask==1.3.0 pytest-cov==4.1.0
pytest
```

## 🐳 Déploiement Docker

```bash
# Construction et lancement
docker-compose up -d

# Accès via http://localhost
```

## 📁 Structure du Projet

```
projet_de_fin/
├── bibmath_rdc/           # Package principal
│   ├── routes/           # Routes (main, auth)
│   ├── templates/        # Templates HTML
│   ├── static/          # CSS, JS, images
│   ├── data/            # Base de données SQLite
│   ├── models.py        # Modèles de données
│   ├── forms.py         # Formulaires WTF
│   ├── config.py        # Configuration
│   └── app.py           # Factory Flask
├── tests/               # Tests unitaires
├── run.py              # Point d'entrée
├── init_db.py          # Initialisation DB
└── requirements.txt    # Dépendances
```

## 🛠️ Guide Développeur

### Ajouter une Nouvelle Route
```python
# Dans bibmath_rdc/routes/main.py
@main_bp.route('/nouvelle-page')
def nouvelle_page():
    return render_template('nouvelle_page.html')
```

### Créer un Nouveau Modèle
```python
# Dans bibmath_rdc/models.py
class NouveauModele(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
```

### Ajouter un Template
```html
<!-- Dans bibmath_rdc/templates/nouvelle_page.html -->
{% extends "base.html" %}
{% block content %}
<h1>Nouvelle Page</h1>
{% endblock %}
```

## 🎨 Fonctionnalités UI

### Mode Sombre
- Bouton de basculement automatique en haut à droite
- Thème sauvegardé dans le navigateur

### Animations
- Cartes avec effet hover
- Transitions fluides
- Animations au scroll

## 🔒 Configuration Sécurisée

### Variables d'Environnement (.env)
```bash
SECRET_KEY=votre-clé-secrète-ici
FLASK_ENV=development
RECAPTCHA_PUBLIC_KEY=votre-clé-publique
RECAPTCHA_PRIVATE_KEY=votre-clé-privée
```

### Rate Limiting
- 5 tentatives de connexion/minute
- 3 inscriptions/heure
- 200 requêtes/jour par IP

## 🧪 Tests

```bash
# Lancer tous les tests
pytest

# Tests avec couverture
pytest --cov=bibmath_rdc

# Tests spécifiques
pytest tests/test_auth.py
```

## 📊 Performance

### Cache Activé
- Résumés: 5 minutes
- Détails: 10 minutes
- Pages statiques: 1 heure

### Optimisations
- Compression CSS/JS
- Images optimisées
- Requêtes SQL optimisées

## 🚨 Dépannage

### Erreur d'Import
```bash
# Si erreur "Module not found"
pip install --upgrade -r bibmath_rdc/requirements.txt
```

### Base de Données
```bash
# Réinitialiser la DB
rm bibmath_rdc/data/bibmath.db
python init_db.py
```

### Port Occupé
```bash
# Changer le port dans run.py
app.run(port=5001)
```

## 📞 Support

- **Email**: support@bibmath.cd
- **Documentation**: README.md
- **Issues**: Créer un ticket GitHub

## 🇨🇩 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit (`git commit -m 'Ajouter nouvelle fonctionnalité'`)
4. Push (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

---
**BibMath RDC** - Plateforme éducative pour la République Démocratique du Congo 🇨🇩