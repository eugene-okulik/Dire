import pytest
import allure
import requests

from endpoints.get_post import GetPost
from endpoints.create_post import CreatePost
from endpoints.update_post import UpdatePost
from endpoints.patch_post import PatchPost
from endpoints.delete_post import DeletePost


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def update_post_endpoint():
    return UpdatePost()


@pytest.fixture()
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


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
