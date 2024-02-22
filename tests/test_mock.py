from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test 1 : Création d'un nouveau coach + vérification de la création
def test_create_coach(mocker):
    """
        Création d'un coach
    """
    mocker.patch(
        "app.actions.create_coach",
        return_value={
            "name": "John",
            "birthdate": "1985-05-20",
            "id": 1,
            "inventory": [],
            "creatures": []
        }
    )
    response = client.post("/coaches/", json={"name": "Alice", "birthdate": "1985-05-20"})
    assert response.status_code == 200
    assert (response.json() ==
            {"name": "Alice", "birthdate": "1985-05-20", "id": 1, "inventory": [], "creatures": []})


def test_get_objects(mocker):
    mocker.patch("app.actions.get_objects",
                 return_value=[
                     {
                         "name": "sword",
                         "description": "sharp weapon",
                         "id": 1,
                         "owner_id": 2
                     },
                     {
                         "name": "shield",
                         "description": "protective gear",
                         "id": 2,
                         "owner_id": 1
                     }
                 ])
    response = client.get("/objects")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_coaches(mocker):
    mocker.patch("app.actions.get_coaches",
                 return_value=[
                     {
                         "name": "Alice",
                         "birthdate": "1985-05-20",
                         "id": 1,
                         "inventory": [],
                         "creatures": []
                     }
                 ])
    response = client.get("/coaches")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_monsters(mocker):
    mocker.patch("app.actions.get_monsters",
                 return_value=[
                     {
                         "api_id": 150,
                         "custom_name": "Monster1",
                         "id": 1,
                         "name": "goblin",
                         "owner_id": 1
                     },
                     {
                         "api_id": 56,
                         "custom_name": "Monster2",
                         "id": 2,
                         "name": "dragon",
                         "owner_id": 2
                     }
                 ])
    response = client.get("/monsters")
    assert response.status_code == 200
    assert len(response.json()) == 2