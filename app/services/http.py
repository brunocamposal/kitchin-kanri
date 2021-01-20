from http import HTTPStatus
import json

## Função de resposta HTTP
def build_api_response(http_status, data='[]') -> tuple:
    return build_response_message(http_status, data), http_status


def build_response_message(http_status, data ) -> dict:
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad request',
        HTTPStatus.CREATED: 'Successfully created',
        HTTPStatus.NOT_FOUND: 'Not found',
        HTTPStatus.OK: 'Ok',
        HTTPStatus.ACCEPTED : 'Deleted'
        
    }

    return {'message': messages[http_status],
            'data': json.loads(data)
        }