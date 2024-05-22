import requests
import allure

from endpoints.base_endpoint import BaseEndpoint


class DeletePost(BaseEndpoint):

    @allure.step('Отправка запроса для удаления поста')
    def delete_post(self, new_object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{new_object_id}', headers=headers)
        return self.response
