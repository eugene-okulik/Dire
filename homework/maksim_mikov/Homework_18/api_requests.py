import requests


def all_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    # print(response)
    assert len(response) == 99, 'Not all posts returned'


# all_posts()


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    assert response.json()['id'] == post_id


# one_post()


def post_a_post():
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'
    print(response.json())


# post_a_post()


def new_post():
    body = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print('clear :', response.json())


def put_a_post():
    post_id = new_post()
    body = {
        "title": "foo-foo 2",
        "body": "bar-bar 2",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    )
    print(response)
    assert response.json()['title'] == "foo-foo 2"
    clear(post_id)


put_a_post()


def patch_a_post():
    post_id = new_post()
    body = {
        "body": "bar-bar 2",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


# patch_a_post()


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)


# delete_a_post()
