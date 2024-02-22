"""
Module implémentant une interface API FastAPI pour la gestion des opérations relatives aux formateurs dans le contexte d'une application Pokémon.

Ce module expose des points d'accès pour créer, récupérer et effectuer des opérations sur les formateurs, ainsi que pour ajouter des objets et des Pokémon à l'inventaire d'un formateur. Ces opérations font appel à des fonctions définies dans les modules 'actions', 'schemas' et 'utils', ainsi qu'à des dépendances.

Classes et objets :
- router : Instance de APIRouter utilisée pour définir les routes de l'API.

Fonctions :
- create_trainer(formateur: schemas.TrainerCreate, base_de_donnees: Session = Depends(get_db))
-> schemas.Trainer:
Point de terminaison POST pour créer un formateur.
Paramètres :
- formateur (schemas.TrainerCreate) : Données du nouveau formateur.
- base_de_donnees (Session) : Session SQLAlchemy pour accéder à la base de données.
Retourne :
- schemas.Trainer : Formateur créé.
"""


from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends, HTTPException
from app.utils.utils import get_db
from app import actions, schemas
router = APIRouter()


@router.post("/", response_model=schemas.Trainer)
def create_trainer(trainer: schemas.TrainerCreate, database: Session = Depends(get_db)):
    """
        Créer un formateur
    """
    return actions.create_trainer(database=database, trainer=trainer)


@router.get("", response_model=List[schemas.Trainer])
def get_trainers(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        retourne tous les formateurs
        limite 100 par défaut
    """
    trainers = actions.get_trainers(database, skip=skip, limit=limit)
    return trainers


@router.get("/{trainer_id}", response_model=schemas.Trainer)
def get_trainer(trainer_id: int, database: Session = Depends(get_db)):
    """
        retourne un formateur par son ID
    """
    db_trainer = actions.get_trainer(database, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db_trainer


@router.post("/{trainer_id}/item/", response_model=schemas.Item)
def create_item_for_trainer(
    trainer_id: int, item: schemas.ItemCreate, database: Session = Depends(get_db)
):
    """
        Ajouter un objet à un formateur
    """
    return actions.add_trainer_item(database=database, item=item, trainer_id=trainer_id)


@router.post("/{trainer_id}/pokemon/", response_model=schemas.Pokemon)
def create_pokemon_for_trainer(
    trainer_id: int, pokemon: schemas.PokemonCreate, database: Session = Depends(get_db)
):
    """
        Add a Pokemon to a trainer
    """
    return actions.add_trainer_pokemon(database=database, pokemon=pokemon, trainer_id=trainer_id)
