from locust import task, HttpUser


class PostUser(HttpUser):

    @task(1)
    def get_all_posts(self):
        self.client.get(
            '/objects',
            headers={"content-type": "application/json"}
        )

    @task(3)
    def get_one_post(self):
        self.client.get(
            '/objects/7',
            headers={"content-type": "application/json"}
        )

    @task(1)
    def add_one_post(self):
        self.client.post(
            '/objects',
            json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            },
            headers={"content-type": "application/json"}
        )

    @task(1)
    def update_one_post(self):
        self.client.put(
            '/objects/7',
            json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB",
                    "color": "silver"
                }
            },
            headers={"content-type": "application/json"}
        )

    @task(1)
    def patch_one_post(self):
        self.client.patch(
            '/objects/7',
            json={
                "name": "Apple MacBook Pro 15",
                "data": {
                    "color": "space"
                }
            },
            headers={"content-type": "application/json"}
        )

    @task(3)
    def delete_one_post(self):
        self.client.delete(
            '/objects/6',
            headers={"content-type": "application/json"}
        )
