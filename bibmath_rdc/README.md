# Bibmath RDC - Plateforme Éducative

Bibmath RDC est une application web moderne dédiée à l'enseignement des mathématiques et de la physique en République Démocratique du Congo. Elle offre des résumés de cours approfondis, des exercices corrigés et un système d'authentification pour les étudiants et enseignants.

## 🚀 Fonctionnalités

- **Résumés de cours** : Des fiches détaillées avec rendu LaTeX impeccable et schémas explicatifs.
- **Banque d'exercices** : Des problèmes triés par sujet et niveau avec solutions cachées/révélables.
- **Rendu Mathématique** : Support complet du LaTeX via MathJax.
- **Authentification** : Inscription et connexion sécurisées.
- **Design Responsive** : Optimisé pour mobile, tablette et desktop.
- **Export PDF** : Possibilité d'exporter les cours pour une lecture hors-ligne.
- **Système de points** : Récompense les étudiants pour leur participation.
- **Gestion des rôles** : Différents niveaux d'accès (étudiant, enseignant, administrateur).

## 🛠️ Technologies Utilisées

- **Backend** : Flask 3.0.0
- **Base de données** : SQLite avec SQLAlchemy
- **Authentification** : Flask-Login
- **Formulaires** : Flask-WTF
- **Rendu Mathématique** : MathJax
- **Frontend** : HTML5, CSS3, JavaScript
- **Templates** : Jinja2

## 📋 Prérequis

- Python 3.8 ou supérieur
- Navigateur web moderne (Chrome, Firefox, Safari, Edge)

## 🛠️ Installation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/votre-repo/bibmath-rdc.git
   cd bibmath-rdc
   ```

2. **Environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate sur Windows
   ```

3. **Dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Base de données** :

   ```bash
   python seed_db.py
   ```

5. **Lancement** :
   ```bash
   python app.py
   ```

L'application sera accessible sur `http://localhost:5000`

## 📖 Utilisation

### Pour les Étudiants

1. Créez un compte ou connectez-vous
2. Parcourez les résumés de cours par matière et niveau
3. Consultez les exercices et révélez les solutions
4. Accumulez des points en participant activement

### Pour les Enseignants

1. Connectez-vous avec un compte enseignant
2. Ajoutez de nouveaux résumés et exercices
3. Gérez le contenu éducatif

### Pour les Administrateurs

1. Accès complet à la gestion des utilisateurs
2. Supervision de tout le contenu

## 🛣️ Routes Disponibles

### Routes Publiques

- `/` - Page d'accueil
- `/resumes` - Liste des résumés (avec filtres par matière)
- `/auth/login` - Connexion
- `/auth/register` - Inscription

### Routes Protégées (Authentification requise)

- `/auth/profile` - Profil utilisateur
- `/auth/logout` - Déconnexion

## 📂 Structure du projet

```
bibmath_rdc/
├── app.py                 # Point d'entrée de l'application
├── models.py              # Modèles de base de données (User, Resume)
├── forms.py               # Formulaires WTForms
├── config.py              # Configuration de l'application
├── seed_db.py             # Script d'initialisation de la base de données
├── requirements.txt       # Dépendances Python
├── routes/
│   ├── __init__.py
│   ├── main.py            # Routes principales
│   └── auth.py            # Routes d'authentification
├── templates/             # Templates HTML
│   ├── base.html          # Template de base
│   ├── index.html         # Page d'accueil
│   ├── login.html         # Page de connexion
│   ├── register.html      # Page d'inscription
│   ├── profile.html       # Profil utilisateur
│   ├── resumes.html       # Liste des résumés
│   └── ...
├── static/                # Assets statiques
│   ├── css/
│   │   └── style.css      # Styles CSS
│   ├── js/
│   │   └── main.js        # Scripts JavaScript
│   └── img/               # Images
└── data/                  # Base de données SQLite
    └── bibmath.db
```

## 🚀 Déploiement

### Développement

```bash
export FLASK_ENV=development
python app.py
```

### Production

Pour un déploiement en production, considérez :

- Utiliser un serveur WSGI comme Gunicorn
- Configurer une base de données plus robuste (PostgreSQL)
- Activer HTTPS
- Configurer les variables d'environnement pour la sécurité

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Directives de contribution

- Respectez les standards PEP 8 pour le code Python
- Ajoutez des tests pour les nouvelles fonctionnalités
- Mettez à jour la documentation si nécessaire
- Utilisez des commits descriptifs

## 📝 Tests

```bash
# Installation des dépendances de test
pip install pytest

# Exécution des tests
pytest
```

## 🐛 Signaler un Bug

Si vous trouvez un bug, veuillez ouvrir une issue sur GitHub avec :

- Description détaillée du problème
- Étapes pour reproduire
- Environnement (OS, version Python, navigateur)
- Captures d'écran si pertinent

## 📞 Support

Pour toute question ou support :

- Email : support@bibmath-rdc.cd
- Documentation : [Lien vers la documentation complète]

## 👥 Auteurs

- **Équipe Bibmath RDC** - _Développement initial_
- **Contributeurs** - Voir [contributors](https://github.com/votre-repo/bibmath-rdc/graphs/contributors)

## 🙏 Remerciements

- Communauté éducative de la RDC
- Bibliothèque MathJax pour le rendu LaTeX
- Framework Flask et ses extensions

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

**Note** : Ce projet est destiné à des fins éducatives et est distribué gratuitement pour soutenir l'éducation en République Démocratique du Congo.

---

⭐ Si ce projet vous aide dans vos études, n'hésitez pas à lui donner une étoile sur GitHub !
