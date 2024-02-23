"""
 Test unitaire mock
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_trainer(mocker):
    """
        Creation d'un trainer
    """
    mocker.patch(
        "app.actions.create_trainer",
        return_value={
            "name": "Younes",
            "birthdate": "1995-11-25",
            "id": 1,
            "inventory": [],
            "pokemons": []
        }
    )
    response = client.post("/trainers/", json={"name": "Younes", "birthdate": "1995-11-25"})
    assert response.status_code == 200
    assert (response.json() ==
            {"name": "Younes", "birthdate": "1995-11-25", "id": 1, "inventory": [], "pokemons": []})


def test_get_items(mocker):
    """
        Recuperation des items
        """
    mocker.patch("app.actions.get_items",
                 return_value=[
                     {
                         "name": "test",
                         "description": "test",
                         "id": 1,
                         "trainer_id": 2
                     },
                     {
                         "name": "test2",
                         "description": "test2",
                         "id": 1,
                         "trainer_id": 1
                     }
                 ])
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_trainers(mocker):
    """
    ²   Recuperation des trainers"""
    mocker.patch("app.actions.get_trainers",
                 return_value=[
                     {
                         "name": "Younes",
                         "birthdate": "1995-12-04",
                         "id": 1,
                         "inventory": [],
                         "pokemons": []
                     }
                 ])
    response = client.get("/trainers")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_pokemon(mocker):
    """
        Recuperation des pokemons
        """
    mocker.patch("app.actions.get_pokemons",
                 return_value=[
                     {
                         "api_id": 150,
                         "custom_name": "test",
                         "id": 1,
                         "name": "mewtwo",
                         "trainer_id": 1
                     },
                     {
                         "api_id": 56,
                         "custom_name": "test2",
                         "id": 2,
                         "name": "mankey",
                         "trainer_id": 2
                     }
                 ])
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert len(response.json()) == 2
