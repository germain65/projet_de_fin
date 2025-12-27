#### Démonstration vidéo : https://youtu.be/URL_A_REMPLACER
#### Description :

BibMath RDC est une application web éducative dédiée à l’apprentissage et à l’enseignement des mathématiques en République Démocratique du Congo. Ce projet a été réalisé comme projet final du cours CS50x 2025 et met en pratique plusieurs notions étudiées tout au long du cours, notamment Python, SQL, HTML, CSS, JavaScript et Flask.

L’objectif principal de BibMath RDC est de faciliter l’accès à des ressources mathématiques structurées et de qualité, en langue française, dans un contexte où les supports pédagogiques numériques restent limités. Le projet vise également à offrir un environnement interactif permettant aux élèves de s’exercer et de s’autoévaluer, tout en donnant aux enseignants des outils simples pour publier du contenu éducatif.

La plateforme propose un système d’authentification, la consultation de résumés de cours, des exercices organisés par chapitres, ainsi que des quiz à choix multiples corrigés automatiquement. BibMath RDC distingue plusieurs rôles utilisateurs (administrateur, professeur et étudiant), afin de contrôler l’accès aux différentes fonctionnalités.

---

## Fonctionnement général du projet

BibMath RDC est une application Flask construite selon le modèle MVC (Model–View–Controller). L’utilisateur interagit avec l’application via une interface web responsive développée avec Bootstrap 5.

Après inscription et connexion, les étudiants peuvent consulter des résumés de cours mathématiques incluant des formules écrites en notation de type LaTeX. Les exercices sont classés par chapitres et catégories, permettant une progression pédagogique cohérente. Les quiz prennent la forme de QCM et sont corrigés automatiquement, avec un score et des explications associées aux réponses, afin de favoriser l’apprentissage plutôt que la simple évaluation.

Les professeurs et administrateurs disposent de fonctionnalités supplémentaires leur permettant de créer, modifier et organiser les contenus pédagogiques. Les administrateurs peuvent également gérer les rôles des utilisateurs.

---

## Fichiers et structure du projet

Le projet est organisé de la manière suivante :

projet_de_fin/
├── bibmath_rdc/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── forms.py
│ ├── routes/
│ │ ├── main.py
│ │ └── auth.py
│ ├── templates/
│ ├── static/
│ └── data/
├── run.py
└── init_db.py

yaml
Copy code

- **app.py** : contient la factory Flask et l’initialisation des extensions (SQLAlchemy, Flask-Login).
- **config.py** : gère la configuration de l’application (clé secrète, base de données).
- **models.py** : définit les modèles de données (utilisateurs, résumés, exercices, quiz).
- **forms.py** : regroupe les formulaires Flask-WTF avec validation et protection CSRF.
- **routes/** : contient les Blueprints séparant les routes principales et l’authentification.
- **templates/** : fichiers HTML utilisant Jinja2 et l’héritage de templates.
- **static/** : fichiers CSS, JavaScript et images.
- **data/** : contient la base de données SQLite.
- **run.py** : point d’entrée pour lancer l’application.
- **init_db.py** : initialise la base de données et crée des comptes de test.

Cette organisation permet une meilleure lisibilité du code et facilite la maintenance du projet.

---

## Choix de conception

Plusieurs choix techniques ont été débattus durant le développement. Flask a été retenu plutôt qu’un framework plus lourd, car il offre une grande flexibilité et reste adapté à un projet éducatif développé par une seule personne. SQLite a été choisie pour sa simplicité d’installation et sa portabilité, tout en laissant la possibilité d’évoluer vers PostgreSQL à l’avenir.

Le modèle MVC a été adopté afin de séparer clairement la logique métier, les données et l’interface utilisateur. Bootstrap 5 a été utilisé pour garantir une interface responsive, un point important étant donné que de nombreux utilisateurs accèdent à internet principalement via un téléphone mobile.

La sécurité a également été prise en compte : les mots de passe sont hashés avec bcrypt, les formulaires sont protégés contre les attaques CSRF et les entrées utilisateur sont validées afin de limiter les vulnérabilités courantes.

---

## Exécution du projet

1. Installer les dépendances :
```bash
pip install -r bibmath_rdc/requirements.txt
Initialiser la base de données :

bash
Copy code
python init_db.py
Lancer l’application :

bash
Copy code
python run.py
Puis ouvrir un navigateur à l’adresse : http://127.0.0.1:5000.

Des comptes de test (administrateur, professeur et étudiant) sont fournis pour faciliter la démonstration.

Conclusion
BibMath RDC représente une application concrète des compétences acquises dans le cadre du cours CS50x. Le projet répond à un problème réel lié à l’accès aux ressources éducatives et démontre l’utilisation combinée du backend, du frontend et d’une base de données. Bien que des améliorations soient possibles, la version actuelle constitue une base fonctionnelle et extensible pour une plateforme éducative adaptée au contexte congolais.
