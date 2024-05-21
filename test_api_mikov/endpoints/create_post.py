import requests
import allure

from endpoints.base_endpoint import BaseEndpoint


class CreatePost(BaseEndpoint):

    @allure.step('Отправка запроса для создания поста')
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
