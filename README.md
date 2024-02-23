# Anas Ikli, Younes Ouartassi, Yacine Kerrad

Plan Des tests : 
https://docs.google.com/document/d/1Z66k990kGvgd-aBt-q1VCxnfxZOu_j1AM7N2Av2_vd4/edit?usp=sharing



## Préparer son environnement

Installer le paquet virtualenv

> pip install virtualenv

Créer l'environnement virtuel

> python -m venv venv

venv correspond au chemin/dossier dans lequel sera activé votre environnement virtuel
(Dans notre cas, dans le dossier où est exécuté la commande, dans le dossier venv)

Activer l'environnement virtuel

> Linux/Mac : source venv/bin/activate
> Windows : ./venv/Scripts/activate

Si sur windows vous ne pouvez exécuter le script en .ps1, ouvrer un powershelle en admin et exécuter
> set-executionpolicy unrestricted

Installer les paquets

> pip install fastapi locust pytest uvicorn coverage httpx pytest-mock pytest-profiling pylint sqlalchemy pydantic

## Démarrer l'application

> uvicorn main:app
> --reload # pour développer (recharge automatique l'application à chaque changement d'un fichier)

Exécuter dans le dossier application

## Pytest

> python -m pytest

## Coverage

> coverage run -m pytest --profile # remplace la commande python
> coverage html # génère le rapport en html

##Pourcentage coverage : 

coverage report --fail-under=90

Exécuter à la racine du dossier

## Locust

> locust -f locust.py

## Pylint

> pylint application/ tests/
