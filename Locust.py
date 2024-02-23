from locust import HttpUser, between, task, TaskSet

class MonUtilisateur(HttpUser):
    wait_time = between(1, 3)

    @task
    class ItemTasks(TaskSet):
        @task
        def get_items(self):
            self.client.get("items")

    @task
    class PokemonTasks(TaskSet):
        @task
        def get_pokemons(self):
            self.client.get("pokemons")

        @task
        def battle_pokemon(self):
            pokemon_id_1 = 1  # Remplacez par un véritable ID de Pokémon
            pokemon_id_2 = 2  # Remplacez par un autre véritable ID de Pokémon
            self.client.get(f"pokemons/battle/{pokemon_id_1}/{pokemon_id_2}")

        @task
        def get_random_pokemons(self):
            self.client.get("pokemons/random")

    @task
    class TrainerTasks(TaskSet):
        @task
        def create_trainer(self):
            trainer_data = {"name": "Nouveau Dresseur", "level": 1}
            self.client.post("trainers/", json=trainer_data)

        @task
        def get_trainers(self):
            self.client.get("trainers")

        @task
        def get_trainer(self):
            trainer_id = 1 
            self.client.get(f"trainers/{trainer_id}")

        @task
        def create_item_for_trainer(self):
            trainer_id = 1  
            item_data = {"name": "Nouvel Objet", "description": "Description de l'objet"}
            self.client.post(f"trainers/{trainer_id}/item/", json=item_data)

        @task
        def create_pokemon_for_trainer(self):
            trainer_id = 1 
            pokemon_data = {"name": "Nouveau Pokémon", "level": 5, "type": "Feu"}
            self.client.post(f"trainers/{trainer_id}/pokemon/", json=pokemon_data)
