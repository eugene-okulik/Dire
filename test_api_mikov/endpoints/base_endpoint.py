import allure


class BaseEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {"content-type": "application/json"}

    @allure.step('Проверка на наличие измененных данных')
    def check_changes(self, expected_data):
        if 'data' in expected_data:
            assert self.json.get('data').get('color') == expected_data['data']['color'], "Color value does not match"
        if 'name' in expected_data:
            assert self.json.get('name') == expected_data['name'], "Name value does not match"

    @allure.step('Проверка статус кода')
    def check_status_code(self):
        assert self.response.status_code == 200, f"Failed to delete object. Status code: {self.response.status_code}"

    @allure.step('Проверка что объект не пустой')
    def check_object_is_not_empty(self):
        assert self.json['id'] is not None, 'Object ID is not found in the response'
