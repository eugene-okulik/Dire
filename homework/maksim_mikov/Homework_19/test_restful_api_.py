import pytest
import requests
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning, module='pkg_resources')


@pytest.fixture()
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
def testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_and_after_test():
    print('before test')
    yield
    print('after test')


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
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    object_id = (response.json()['id'])
    assert response.status_code == 200, f"Failed to create object. Status code: {response.status_code}"
    assert object_id is not None, 'Object ID is not found in the response'


def test_get_object_to_id(before_and_after_test, new_object_id):
    response = requests.get(
        f'https://api.restful-api.dev/objects/{new_object_id}'
    )
    assert response.json().get('id') == new_object_id


@pytest.mark.critical
def test_update_object(before_and_after_test, new_object_id):
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
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())
    assert response.json().get('data').get('color') == 'silver'


@pytest.mark.medium
def test_patch_object(before_and_after_test, new_object_id):
    payload = {
        "name": "Apple MacBook Pro 15",
        "data": {
            "color": "space"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())
    assert response.json().get('data').get('color') == 'space'
    assert response.json().get('name') == 'Apple MacBook Pro 15'


def test_delete_object(before_and_after_test, new_object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    print(response.json())
    print(response.status_code)
