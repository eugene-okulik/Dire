import requests
import allure

from endpoints.base_endpoint import BaseEndpoint


class UpdatePost(BaseEndpoint):

    @allure.step('Отправка запроса для изменения поста')
    def make_changes_in_post(self, new_object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
