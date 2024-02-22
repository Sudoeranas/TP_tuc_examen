"""
Module contenant une API routeur FastAPI pour la gestion des
opérations liées aux pokémons dans une application de formation
de Pokémon.
- pokemons_battle(id_pokemon_api_1: int, id_pokemon_api_2: int) -> dict:
    Point de terminaison GET pour une bataille entre deux Pokémon.
    Paramètres :
        - id_pokemon_api_1 (int) : ID du premier Pokémon.
        - id_pokemon_api_2 (int) : ID du deuxième Pokémon.
    Retourne :
        - dict : Résultat de la bataille sous forme de dictionnaire.
        {"idPokemonAPI": idPokemonAPI, "resultat": valeurResultat:int}
        (Match nul en cas d'égalité).

- pokemons_random() -> List[dict]:
    Point de terminaison GET pour obtenir 3 Pokémon choisis aléatoirement.
    Retourne :
        - List[dict] : Liste de 3 Pokémon avec leurs données.
"""
from random import randint
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.utils import get_db
from app import actions, schemas
from app.utils.pokeapi import battle_pokemon, get_pokemon_data

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons


@router.get("/battle/{pokemon_api_id_1}/{pokemon_api_id_2}")
def pokemons_battle(pokemon_api_id_1: int, pokemon_api_id_2: int):
    """
        Battle between two pokemons
        Params:
            pokemonID (int): id of the first pokemon
            pokemonID2 (int): id of the second pokemon
        Return result
            {"pokemonApiID": pokemonApiID, "result": resultValue:int}
    """
    return battle_pokemon(pokemon_api_id_1, pokemon_api_id_2)


@router.get("/random/")
def pokemons_random():
    """
        Get 5 random pokemons
        Return:
            List of 5 randomass pokemons
    """
    pokemons: list[dict, dict, dict] = []
    while len(pokemons) != 5:
        pokemon = get_pokemon_data(randint(1, 898))
        if pokemon not in pokemons and pokemon is not None:
            pokemons.append(pokemon)
    return pokemons
