# Blog Logger Python

Ce projet Python propose une structure simple et claire intégrant un système de logging centralisé avec écriture dans des fichiers rotatifs. Il est adapté aux projets de traitement de données, d'analyse ou de scripts automatisés.

## Fonctionnalités principales
- Logger central configurable via `logger.py`
- Écriture des logs en console et dans un fichier tournant `logs/application.log`
- Exemple de module de traitement et de fonction utilitaire
- Fichier de données d'exemple (CSV)
- Tests unitaires de base

## Lancement

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Exécuter le projet :
```bash
python main.py
```

Les logs apparaissent dans le terminal **et** dans le fichier `logs/application.log`.

## Structure

```
mon_projet/
├── main.py                  # Point d'entrée
├── config/logger.py         # Logger central
├── core/                    # Modules logiques
├── data/                    # Données d'entrée
├── logs/                    # Dossier des logs
├── tests/                   # Tests unitaires
├── requirements.txt         # Dépendances
├── README.md                # Documentation
```

## Auteur
Emmanuel Jakobowicz
