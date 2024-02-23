"""
locustfile.py
A simple locust file that does a get request to the home page
"""

from locust import HttpUser, task, between


class User(HttpUser):
    """
    A user class that does a simple get request to the home page
    """
    wait_time = between(2, 5)

    @task
    def get_home(self):
        """
        A task that does a get request to the home page
        """
        self.client.get("/5")