# Token Grabber Discord

## Description

Ce projet est un script Python conçu pour récupérer les tokens Discord d'un utilisateur à partir de ses fichiers locaux. Il décrypte les tokens et les envoie à un webhook Discord spécifié. Ce script est à des fins éducatives uniquement.

## Fonctionnalités

- Récupère les tokens Discord stockés dans les fichiers locaux.
- Décrypte les tokens récupérés.
- Envoie les informations sur les tokens à un webhook Discord.
- Récupère et affiche des informations sur l'utilisateur Discord.
- Envoie les informations de l'ordinateur local (IP publique, IP locale, nom du PC).

## Prérequis

- Python 3.x
- Bibliothèques Python : `requests`, `Cryptodome`, `win32crypt`, `json`

## Installation des dépendances

Pour installer les dépendances nécessaires, exécutez la commande suivante :

```bash
pip install -r requirements.txt
```

## Note
Il peut y avoir deds conflits entre certaine librairies notament entre ```pycrypto``` et ```pycryptodome```, le meilleur moyen est de désinstaller ```pycrypto``` et de garder seulement ```pycryptodome```
