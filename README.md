# BibMath RDC - Plateforme Éducative

## Installation

1. **Installer les dépendances :**
```bash
cd projet_de_fin
pip install -r bibmath_rdc/requirements.txt
```

2. **Initialiser la base de données :**
```bash
python init_db.py
```

3. **Lancer l'application :**
```bash
python run.py
```

4. **Accéder à l'application :**
Ouvrir http://127.0.0.1:5000 dans votre navigateur

## Comptes de test

- **Admin :** admin@bibmath.cd / admin123
- **Professeur :** kambale@bibmath.cd / prof123
- **Étudiant :** etudiant1@bibmath.cd / student123

## Structure du projet

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
├── run.py               # Point d'entrée
└── init_db.py          # Initialisation DB
```

## Fonctionnalités

- ✅ Authentification (inscription/connexion)
- ✅ Résumés de cours avec LaTeX
- ✅ Exercices organisés par catégories
- ✅ Quizzes interactifs
- ✅ Interface responsive Bootstrap 5
- ✅ Base de données SQLite

## Erreurs corrigées

1. **Imports relatifs** - Tous les imports ont été corrigés
2. **Templates manquants** - Créés : create_quiz.html, add_question.html, take_quiz.html
3. **Navigation** - Ajout du menu utilisateur dans base.html
4. **Structure** - Réorganisation en package Python proper
5. **Scripts** - Création de run.py et init_db.py pour faciliter l'utilisation