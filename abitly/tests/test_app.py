import pytest
from flask import json

# Flask App
from abitly import create_app


@pytest.fixture
def app():
    app = create_app()

    return app


def test_app_should_responds_ok(client):
    """Should respond OK when is requested by GET method"""

    response = client.get('/')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = f'ABitly is running'

    assert response.status_code == 200
    assert response_body['status'] == 'OK'
    assert response_body['statusCode'] == 200
    assert response_body['message'] == expected_message


def test_app_should_responds_not_found(client):
    """Should respond NotFound when is requested by GET method
    and unexpected parameters
    """

    response = client.get('/a')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = ('The requested URL was not found on the server. '
                        'If you entered the URL manually please check '
                        'your spelling and try again.').format()

    assert response.status_code == 404
    assert response_body['status'] == 'Not Found'
    assert response_body['statusCode'] == 404
    assert response_body['errorMessage'] == expected_message


def test_app_should_responds_method_not_allowed(client):
    """Should respond MethodNotAllowed when is requested by different
    method of GET
    """

    response = client.post('/')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = 'The method is not allowed for the requested URL.'

    assert response.status_code == 405
    assert response_body['status'] == 'Method Not Allowed'
    assert response_body['statusCode'] == 405
    assert response_body['errorMessage'] == expected_message
