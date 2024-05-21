import requests
import allure

from endpoints.base_endpoint import BaseEndpoint


class GetPost(BaseEndpoint):

    @allure.step('Получение поста по id')
    def get_object_to_id(self, new_object_id):
        self.response = requests.get(f'{self.url}/{new_object_id}')
        self.json = self.response.json()
        return self.response

    def check_id(self, new_object_id):
        assert self.json.get('id') == new_object_id
