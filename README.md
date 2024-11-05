# data-pipeline

## Description

**data-pipeline** est un projet Python conçu pour traiter des images en les redimensionnant et en les remplissant pour garantir qu'elles soient au format carré. Les images traitées sont sauvegardées dans un dossier unique horodaté, placé dans un dossier `datasets` à la racine du projet. Ce projet utilise la bibliothèque Pillow pour la manipulation d'images et offre une manière simple de gérer un pipeline de traitement d'images.

## Fonctionnalités

- Redimensionnement des images tout en conservant le ratio d'aspect.
- Ajout de padding de couleur unie pour garantir que l'image soit carrée.
- Sauvegarde des images traitées dans un dossier identifié par un horodatage unique.

## Installation

1. **Cloner le dépôt :**

  ```bash
  git clone <url_du_dépôt>
  cd data-pipeline
  ```

2. **Créer un environnement virtuel :**

  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
  ```

3. **Installer les dépendances :**

  ```bash
  pip install -r requirements.txt
  ```


## Utilisation

1. **Ajouter vos images** dans le dossier source spécifié (par exemple `input_images`).

2. **Exécuter le script principal :**

  ```bash
  python main.py
  ```

  Le script traitera toutes les images dans le dossier spécifié et sauvegardera les images redimensionnées et remplies dans un dossier horodaté dans `datasets/`.


## Configuration de Black pour le formatage

Pour garantir un code bien formaté, utilisez **Black** :

```bash
black .
```

## Dépendances

- **Python 3.11**
- **Pillow**
- **datetime**
