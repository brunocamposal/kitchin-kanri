from http import HTTPStatus

# Função de resposta HTTP


def build_api_response(http_status) -> tuple:
    return build_response_message(http_status), http_status


def build_response_message(http_status) -> dict:
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad request',
        HTTPStatus.CREATED: 'Successfully created',
        HTTPStatus.NOT_FOUND: 'Not found',
        HTTPStatus.OK: 'ok',
        HTTPStatus.UNAUTHORIZED: 'Unauthorized',
        HTTPStatus.UNPROCESSABLE_ENTITY: 'User e-mail already in use',
        HTTPStatus.OK: 'Ok',
    }

    return {'message': messages[http_status]}
