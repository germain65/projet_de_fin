```markdown
# BibMath RDC – Plateforme éducative mathématique

#### Video Demo: https://youtu.be/URL_DE_LA_VIDEO

## Description

BibMath RDC est une application web éducative dédiée à l’apprentissage et à l’enseignement des mathématiques en République Démocratique du Congo. Ce projet a été réalisé comme projet final du cours CS50x 2025 et met en pratique plusieurs notions étudiées tout au long du cours, notamment Python, SQL, HTML, CSS, JavaScript et le framework Flask.

L’objectif principal de BibMath RDC est de faciliter l’accès à des ressources mathématiques structurées et de qualité, en langue française, dans un contexte où les supports pédagogiques numériques sont encore limités. Le projet vise également à offrir un environnement interactif permettant aux élèves de s’exercer, de s’autoévaluer et de progresser à leur rythme, tout en fournissant aux enseignants des outils simples pour publier et organiser du contenu pédagogique.

La plateforme propose un système d’authentification, la consultation de résumés de cours, des exercices organisés par chapitres et catégories, ainsi que des quiz à choix multiples corrigés automatiquement. Plusieurs rôles utilisateurs sont implémentés (administrateur, professeur et étudiant) afin de contrôler l’accès aux fonctionnalités et de garantir une gestion cohérente du contenu.

## Fonctionnement général du projet

BibMath RDC est une application Flask construite selon le modèle MVC (Model–View–Controller). L’utilisateur interagit avec l’application à travers une interface web responsive développée avec Bootstrap 5, ce qui permet une utilisation confortable aussi bien sur ordinateur que sur téléphone mobile.

Après inscription et connexion, les étudiants peuvent consulter des résumés de cours mathématiques incluant des formules écrites en notation de type LaTeX, facilitant la compréhension des concepts abordés. Les exercices sont organisés par chapitres et catégories, permettant une progression pédagogique logique. Les quiz prennent la forme de QCM et sont corrigés automatiquement. Un score est affiché ainsi que des explications associées à chaque réponse, afin de favoriser l’apprentissage plutôt que la simple évaluation.

Les professeurs et administrateurs disposent de fonctionnalités supplémentaires leur permettant de créer, modifier et organiser les résumés, exercices et quiz. Les administrateurs peuvent également gérer les rôles des utilisateurs.

## Structure des fichiers du projet

Le projet est organisé de la manière suivante :

```

projet_de_fin/
├── bibmath_rdc/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── forms.py
│   ├── routes/
│   │   ├── main.py
│   │   └── auth.py
│   ├── templates/
│   ├── static/
│   └── data/
├── run.py
└── init_db.py

````

- **app.py** : contient la factory Flask et l’initialisation des extensions (SQLAlchemy, Flask-Login).
- **config.py** : gère la configuration générale de l’application (clé secrète, paramètres de base de données).
- **models.py** : définit les modèles de données (utilisateurs, résumés de cours, exercices, quiz et questions).
- **forms.py** : regroupe les formulaires Flask-WTF avec validation et protection CSRF.
- **routes/** : contient les Blueprints séparant les routes principales et les routes d’authentification.
- **templates/** : fichiers HTML utilisant Jinja2 avec héritage de templates.
- **static/** : fichiers CSS, JavaScript et images.
- **data/** : contient la base de données SQLite.
- **run.py** : point d’entrée permettant de lancer l’application.
- **init_db.py** : script d’initialisation de la base de données et de création des comptes de test.

Cette organisation a été choisie afin d’améliorer la lisibilité du code, la modularité et la facilité de maintenance du projet.

## Choix de conception

Plusieurs décisions techniques ont été prises durant le développement. Flask a été choisi plutôt qu’un framework plus lourd, car il offre une grande flexibilité et reste adapté à un projet éducatif développé par une seule personne. SQLite a été retenue comme base de données pour sa simplicité d’installation et sa portabilité, tout en permettant une migration future vers une solution plus robuste si nécessaire.

Le modèle MVC a été adopté afin de séparer clairement la logique métier, la gestion des données et l’interface utilisateur. Bootstrap 5 a été utilisé pour garantir une interface responsive, un point essentiel étant donné que de nombreux utilisateurs accèdent à internet principalement via un téléphone mobile.

La sécurité a également été prise en compte : les mots de passe sont hashés avec bcrypt, les formulaires sont protégés contre les attaques CSRF et les entrées utilisateur sont validées afin de limiter les vulnérabilités courantes.

## Exécution du projet

1. Installer les dépendances :
```bash
pip install -r bibmath_rdc/requirements.txt
````

2. Initialiser la base de données :

```bash
python init_db.py
```

3. Lancer l’application :

```bash
python run.py
```

Puis ouvrir un navigateur à l’adresse suivante :
`http://127.0.0.1:5000`

Des comptes de test (administrateur, professeur et étudiant) sont fournis afin de faciliter la démonstration du projet.

## Conclusion

BibMath RDC constitue une application concrète des compétences acquises dans le cadre du cours CS50x. Le projet répond à un problème réel lié à l’accès aux ressources éducatives et démontre l’utilisation conjointe du backend, du frontend et d’une base de données relationnelle. Bien que des améliorations soient possibles, la version actuelle offre une base fonctionnelle, claire et extensible pour une plateforme éducative adaptée au contexte congolais.

```
```
