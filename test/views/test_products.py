from test import app
import json


def test_Products_GET_request(app):
    # with app.test_client() as client:
    #     response = client.get('/products')

    #     data = json.loads(response.data.decode())

    #     assert data == {'data':
    #                     [
    #                         {"category_id": 1, "description": "Suco natural de laranja",
    #                             "id": 29, "name": "Suco de laranja", "price": 4.75},
    #                         {"category_id": 3, "description": "Suco natural de laranja",
    #                             "id": 27, "name": "lasanha", "price": 100.0}
    #                     ]}

    #     assert response.status_code == 200


def test_Products_GET_ID_request(app):
    # with app.test_client() as client:
    #     response = client.get('/products/29')

    #     data = json.loads(response.data.decode())

    #     assert data == {"data":
    #                     {"category_id": 1, "description": "Suco natural de laranja",
    #                         "id": 29, "name": "Suco de laranja", "price": 4.75}
    #                     }

    #     assert response.status_code == 200


def test_Products_POST_request(app):
    # with app.test_client() as client:
    #     response = client.post(
    #         '/products',
    #         data=json.dumps(dict(
    #             name='Sucosss',
    #             price=4.75,
    #             description='Suco',
    #             category_id=1,
    #             image='opa.jpg'
    #         )),
    #         content_type='application/json',
    #     )

    #     data = json.loads(response.data.decode())
    #     assert response.status_code == 201
    #     assert 'Successfully created' in data.get("message")


def test_Product_PUT_request(app):
    # with app.test_client() as client:
    #     response = client.put(
    #         '/products/29',
    #         data=json.dumps(dict(
    #             description='Suco',
    #         )),
    #         content_type='application/json',
    #     )

    #     data = json.loads(response.data.decode())
    #     assert response.status_code == 200

    #     assert data == {"data":
    #                     {"category_id": 1, "description": "Suco",
    #                         "id": 29, "name": "Suco de laranja", "price": 4.75}
    #                     }


def test_Products_DELETE_request(app):
    # with app.test_client() as client:
    #     response = client.delete('/products/39')

    #     data = json.loads(response.data.decode())
    #     assert response.status_code == 200
    #     assert 'ok' in data.get("message")
