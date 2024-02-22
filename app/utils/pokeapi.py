import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return False

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    if premier_pokemon and second_pokemon:
        battle_result = battle_compare_stats(premier_pokemon["stats"], second_pokemon["stats"])
        if battle_result > 0:
            return {"Result": first_api_id}
        if battle_result < 0:
            return {"Result": second_api_id}
        return {"Result": "Draw"}
    return None

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    result = 0
    for index, stats in enumerate(first_pokemon_stats):
        result += stats["base_stat"] - second_pokemon_stats[index]["base_stat"]
    return result