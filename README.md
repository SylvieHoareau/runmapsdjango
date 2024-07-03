# runmapsdjango
## Description
**Atlas de la forêt | La Réunion** est une application web interactive offrant des informations détaillées sur les forêts de La Réunion. Le site propose des cartes des domaines forestiers publics et des circuits de randonnées, permettant aux utilisateurs de découvrir la richesse naturelle de l'île.

## Table des matières
- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Auteur](#auteur)

## Fonctionnalités
- **Accueil :** Page d'accueil présentant le projet.
- **Domaine forestier :** Carte des domaines forestiers publics de La Réunion.
- **Randonnées :** Carte des circuits de randonnées classées par niveau de difficulté.
- **Responsive Design :** Adaptation de l'affichage pour les mobiles et tablettes.

## Technologies Utilisées
- **Frontend :**
  - HTML5
  - CSS3 (utilisation de Tailwind CSS)
  - JavaScript
- **Backend :**
  - Django (Python)
- **Autres :**
  - Unsplash API pour les images

## Installation

### Prérequis
- Python 3.x
- pip (gestionnaire de paquets Python)
- Virtualenv (optionnel, mais recommandé)

### Étapes d'installation
1. Clonez le repository :
    ```bash
    git clone https://github.com/votre-utilisateur/atlas-foret-reunion.git
    cd atlas-foret-reunion
    ```

2. Créez et activez un environnement virtuel (optionnel) :
    ```bash
    python3 -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

6. Accédez à l'application via `http://127.0.0.1:8000` dans votre navigateur.

## Utilisation
1. Visitez la page d'accueil pour une introduction au projet.
2. Explorez la carte des domaines forestiers et découvrez les différentes zones forestières.
3. Consultez la carte des circuits de randonnées pour planifier vos sorties.

## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre les étapes suivantes :
1. Fork le repository.
2. Créez une nouvelle branche (`git checkout -b feature/nouvelle-fonctionnalité`).
3. Effectuez vos modifications et commitez (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Pushez votre branche (`git push origin feature/nouvelle-fonctionnalité`).
5. Ouvrez une Pull Request.

## Licence
Ce projet est sous licence GNU GPL3. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteur
**Sylvie HOAREAU**
- [GitHub](https://github.com/votre-utilisateur)
- [LinkedIn](https://www.linkedin.com/in/votre-utilisateur/)

Merci de visiter et d'utiliser **Atlas de la forêt | La Réunion** ! 🌳


