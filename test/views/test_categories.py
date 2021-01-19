
import requests
import pytest
import json


@pytest.fixture(scope="function")
def app():
    return create_app()


def test_GET_request_categories(app):

    categories = app.test_client()

    expected = categories.get('/categories').status_code

    result = 200

    assert expected == result


def test_GET_request_one_category(app):

    category = app.test_client()

    expected = category.get('/categories/7').status_code

    result = 200
    
    assert expected == result

def test_POST_request_categories(requests_mock):

    data = json.dumps({'name':'Cachaça'})
    requests_mock.post('/categories', text=data)
    
    result = 201

    assert expected == result

