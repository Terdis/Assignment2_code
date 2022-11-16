from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        # self.client.get("0.0/3.14")
        self.client.get("?min_max=0.0_3.14")
