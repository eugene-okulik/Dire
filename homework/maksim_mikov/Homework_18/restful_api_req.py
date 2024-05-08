import requests


def new_object():
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
    print(response.json()['id'])
    return response.json()['id']


def clear(object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print('clear :', response.json())


def update_object():
    object_id = new_object()
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
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())
    assert response.json().get('data').get('color') == 'silver'
    clear(object_id)


# update_object()


def patch_object():
    object_id = new_object()
    payload = {
        "name": "Apple MacBook Pro 15",
        "data": {
            "color": "space"
        }
    }
    headers = {"content-type": "application/json"}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    )
    print(response.json())
    assert response.json().get('data').get('color') == 'space'
    assert response.json().get('name') == 'Apple MacBook Pro 15'
    clear(object_id)


# patch_object()


def delete_object():
    object_id = new_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    print(response.json())
    print(response.status_code)


# delete_object()
