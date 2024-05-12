import pytest
import requests
import warnings
import allure


@pytest.fixture()
@allure.title("Подготовка к тесту")
def new_object_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    object_id = (response.json()['id'])
    print('add new object')
    yield object_id
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print('clear :', response.json())


@pytest.fixture(scope='session')
@allure.title("Подготовка к тесту")
def testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
@allure.title("Подготовка к тесту")
def before_and_after_test():
    print('before test')
    yield
    print('after test')


@allure.feature('Posts')
@allure.story('Create posts')
@allure.title('Создание постов')
@pytest.mark.parametrize('payload', [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Apple MacBook Pro 15",
        "data": {
            "year": 2020,
            "price": 1549.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Apple MacBook Pro 14",
        "data": {
            "year": 2021,
            "price": 1349.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
])
def test_new_object(testing, before_and_after_test, payload):
    headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса для создания поста'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
        object_id = (response.json()['id'])
    with allure.step('Проверка кода запроса'):
        assert response.status_code == 200, f"Failed to create object. Status code: {response.status_code}"
    with allure.step('Проверка что объект не пустой'):
        assert object_id is not None, 'Object ID is not found in the response'


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение поста по id')
def test_get_object_to_id(before_and_after_test, new_object_id):
    response = requests.get(
        f'https://api.restful-api.dev/objects/{new_object_id}'
    )
    assert response.json().get('id') == new_object_id


@allure.feature('Posts')
@allure.story('Change posts')
@allure.title('Изменение поста')
@pytest.mark.critical
def test_update_object(before_and_after_test, new_object_id):
    with allure.step('Подготовка тестовых данных'):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
    headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса для создания поста'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{new_object_id}',
            json=payload,
            headers=headers
        )
    print(response.json())
    with allure.step('Проверка на наличие измененных данных'):
        assert response.json().get('data').get('color') == 'silver'


@allure.feature('Posts')
@allure.story('Change posts')
@allure.title('Частичное изменение поста')
@pytest.mark.medium
def test_patch_object(before_and_after_test, new_object_id):
    with allure.step('Подготовка тестовых данных'):
        payload = {
            "name": "Apple MacBook Pro 15",
            "data": {
                "color": "space"
            }
        }
    headers = {"content-type": "application/json"}
    with allure.step('Отправка запроса для создания поста'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{new_object_id}',
            json=payload,
            headers=headers
        )
    print(response.json())
    with allure.step('Проверка на наличие измененных данных'):
        assert response.json().get('data').get('color') == 'space'
        assert response.json().get('name') == 'Apple MacBook Pro 15'


@allure.feature('Posts')
@allure.story('Delete posts')
@allure.title('Удаление поста')
def test_delete_object(before_and_after_test, new_object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200, f"Failed to delete object. Status code: {response.status_code}"


@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.regression
def test_one():
    assert 1 == 1


@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.regression
def test_three():
    assert 1 == 1
