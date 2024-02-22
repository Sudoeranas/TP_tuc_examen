from locust import HttpUser, between, task, TaskSet

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    class ObjectTasks(TaskSet):
        @task
        def fetch_objects(self):
            self.client.get("/objects")

    @task
    class CreatureTasks(TaskSet):
        @task
        def get_creatures(self):
            self.client.get("/creatures")

        @task
        def battle_creature(self):
            creature_id_1 = 1  # Remplacez par un véritable ID de créature
            creature_id_2 = 2  # Remplacez par un autre véritable ID de créature
            self.client.get(f"/creatures/battle/{creature_id_1}/{creature_id_2}")

        @task
        def get_random_creatures(self):
            self.client.get("/creatures/random")

    @task
    class TrainerTasks(TaskSet):
        @task
        def create_coach(self):
            coach_info = {"name": "New Coach", "level": 1}
            self.client.post("/coaches/", json=coach_info)

        @task
        def get_coaches(self):
            self.client.get("/coaches")

        @task
        def get_coach(self):
            coach_id = 1  # Remplacez par un véritable ID de coach
            self.client.get(f"/coaches/{coach_id}")

        @task
        def create_item_for_coach(self):
            coach_id = 1  
            item_info = {"name": "New Item", "description": "Item Description"}
            self.client.post(f"/coaches/{coach_id}/item/", json=item_info)

        @task
        def create_creature_for_coach(self):
            coach_id = 1 
            creature_info = {"name": "New Creature", "level": 5, "type": "Fire"}
            self.client.post(f"/coaches/{coach_id}/creature/", json=creature_info)
