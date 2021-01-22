from test import app
import json


def test_Order_GET_request(app):
    """with app.test_client() as client:
        response = client.get('/orders')

        data = json.loads(response.data.decode())

        assert data == {'data': 
        [
            {'date': '2021-01-18T13:19:43', 'id': 2, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:23:40', 'id': 3, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido Concluído', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:24:07', 'id': 4, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:25:51', 'id': 5, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:26:13', 'id': 6, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:27:07', 'id': 7, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:27:40', 'id': 8, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:31:16', 'id': 9, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
            {'date': '2021-01-18T13:38:14', 'id': 10, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}
        ]} 

        assert response.status_code == 200 """


def test_Order_GET_ID_request(app):
    """with app.test_client() as client:
        response = client.get('/orders/2')

        data = json.loads(response.data.decode())

        assert data == {'data': 
            {'date': '2021-01-18T13:19:43', 'id': 2, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido em andamento', 'total_price': 0.0}, 
        } 

        assert response.status_code == 200 """


def test_Order_POST_request(app):
    """ with app.test_client() as client:
        response = client.post(
            '/orders',
            data=json.dumps(dict(
                status='Pedido em andamento',
                payment_method='dinheiro',
                products=[],
                total_price=5.75
            )),
            content_type='application/json',
        )

        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert 'Successfully created' in data.get("message")"""


def test_Order_PUT_request(app):
    """with app.test_client() as client:
        response = client.put(
            '/orders/3',
            data=json.dumps(dict(
                status='Pedido Concluído',
            )),
            content_type='application/json',
        )

        data = json.loads(response.data.decode())
        assert response.status_code == 200

        assert data == {'data': 
            {'date': '2021-01-18T13:23:40', 'id': 3, 'payment_method': 'dinheiro', 'products': [], 'status': 'Pedido Concluído', 'total_price': 0.0} 
            } """


def test_Order_DELETE_request(app):
    """with app.test_client() as client:
        response = client.delete('/orders/11')

        data = json.loads(response.data.decode())
        assert response.status_code == 200 
        assert 'ok' in data.get("message") """
