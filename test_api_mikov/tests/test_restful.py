import pytest
import allure


TEST_DATA = [
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
]


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение поста по id')
def test_get_object_to_id(testing, before_and_after_test, get_post_endpoint, new_object_id):
    get_post_endpoint.get_object_to_id(new_object_id)
    get_post_endpoint.check_id(new_object_id)


@allure.feature('Posts')
@allure.story('Create posts')
@allure.title('Создание постов')
@pytest.mark.parametrize('payload', TEST_DATA)
def test_new_object(before_and_after_test, create_post_endpoint, payload):
    create_post_endpoint.create_new_post(payload)
    create_post_endpoint.check_status_code()
    create_post_endpoint.check_object_is_not_empty()


@allure.feature('Posts')
@allure.story('Change posts')
@allure.title('Изменение поста')
@pytest.mark.critical
def test_update_object(before_and_after_test, update_post_endpoint, new_object_id):
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
    update_post_endpoint.make_changes_in_post(new_object_id, payload)
    update_post_endpoint.check_changes(payload)


@allure.feature('Posts')
@allure.story('Change posts')
@allure.title('Частичное изменение поста')
@pytest.mark.medium
def test_patch_object(before_and_after_test, patch_post_endpoint, new_object_id):
    with allure.step('Подготовка тестовых данных'):
        payload = {
            "name": "Apple MacBook Pro 15",
            "data": {
                "color": "space"
            }
        }
    patch_post_endpoint.make_partial_changes_in_post(new_object_id, payload)
    patch_post_endpoint.check_changes(payload)


@allure.feature('Posts')
@allure.story('Delete posts')
@allure.title('Удаление поста')
def test_delete_object(before_and_after_test, delete_post_endpoint, new_object_id):
    delete_post_endpoint.delete_post(new_object_id)
    delete_post_endpoint.check_status_code()
