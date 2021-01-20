
import requests
import pytest
import json
from test import app


def test_GET_request_categories(app):

    categories = app.test_client()

    expected = categories.get('/categories').status_code

    result = 200

    assert expected == result


def test_GET_request_one_category(app):

    category = app.test_client()

    expected = category.get('/categories/3').status_code

    result = 200
    
    assert expected == result

def test_POST_request_categories(app):


    with app.test_client() as client:
        response = client.post(
            '/categories',
            data=json.dumps(dict(
                name='Sobremesa',
                image='url'
            )),
            content_type='application/json',
        )

        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert 'Successfully created' in data.get("message")


def test_PATCH_request_categories(app):

    with app.test_client() as client:
        response = client.patch(
            '/categories/3',
            data=json.dumps(dict(
                name='Porções',
            )),
            content_type='application/json',
        )

        data = json.loads(response.data.decode())
        assert response.status_code == 200

        assert data == {"data": {"id": 3, "name": "Porções"},"message": "Ok" }
        


def test_DELETE_request_categories(app):

    with app.test_client() as client:
        response = client.delete('/categories/5')

        data = json.loads(response.data.decode())
        assert response.status_code == 404 
        