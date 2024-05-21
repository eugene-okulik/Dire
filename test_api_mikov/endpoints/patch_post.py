import requests
import allure

from endpoints.base_endpoint import BaseEndpoint


class PatchPost(BaseEndpoint):

    @allure.step('Отправка запроса для частичного изменения поста')
    def make_partial_changes_in_post(self, new_object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Проверка на наличие измененных данных')
    def check_changes(self, expected_data):
        if 'data' in expected_data:
            assert self.json.get('data').get('color') == expected_data['data']['color'], "Color value does not match"
        if 'name' in expected_data:
            assert self.json.get('name') == expected_data['name'], "Name value does not match"
