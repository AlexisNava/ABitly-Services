import pytest
from flask import json

# Flask App
from abitly import create_app


@pytest.fixture
def app():
    app = create_app()

    return app


def test_create_link_should_responds_created(client):
    """Should responds Created when makes a request with
    a valid request body
    """

    request_body = {
        'originalUrl': 'https://discordapp.com/'
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.post('/link/', data=json.dumps(request_body),
                           headers=headers)
    response_body = json.loads(response.get_data(as_text=True))

    assert response.status_code == 201
    assert response_body['statusCode'] == 201
    assert response_body['status'] == 'Created'
    assert len(response_body['generatedUrl']) == 7
    assert response_body['originalUrl'] == 'https://discordapp.com/'


def test_create_link_should_responds_bad_request(client):
    """Should responds BadRequest when makes a request with
    an invalid request body
    """

    request_body = {
        'originalUrl': 543543
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.post('/link/', data=json.dumps(request_body),
                           headers=headers)
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = ('The browser (or proxy) sent a request that this '
                        'server could not understand.').format()

    assert response.status_code == 400
    assert response_body['status'] == 'Bad Request'
    assert response_body['statusCode'] == 400
    assert response_body['errorMessage'] == expected_message


def test_create_link_should_responds_method_not_allowed(client):
    """Should responds MethodNotAllowed when makes a request with
    a different method of POST
    """

    request_body = {
        'originalUrl': 'https://discordapp.com/'
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = client.put('/link/', data=json.dumps(request_body),
                          headers=headers)
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = 'The method is not allowed for the requested URL.'

    assert response.status_code == 405
    assert response_body['status'] == 'Method Not Allowed'
    assert response_body['statusCode'] == 405
    assert response_body['errorMessage'] == expected_message


def test_redirect_to_original_url_should_responds_bad_request(client):
    """Should responds BadRequest when the generated url don't have and
    exactly length of 7 characters
    """

    response = client.get('/link/4RjLzNFg')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = ('The browser (or proxy) sent a request that this '
                        'server could not understand.').format()

    assert response.status_code == 400
    assert response_body['status'] == 'Bad Request'
    assert response_body['statusCode'] == 400
    assert response_body['errorMessage'] == expected_message


def test_redirect_to_original_url_should_responds_not_found(client):
    """Should responds NotFound when not found the
    generated_url in the links table
    """

    response = client.get('/link/1234567')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = ('The requested URL was not found on the server. '
                        'If you entered the URL manually please check '
                        'your spelling and try again.').format()

    assert response.status_code == 404
    assert response_body['status'] == 'Not Found'
    assert response_body['statusCode'] == 404
    assert response_body['errorMessage'] == expected_message


def test_redirect_to_original_url_should_responds_method_not_allowed(client):
    """Should responds MethodNotAllowed when makes a request with
    a different method of GET
    """

    response = client.delete('/link/1234567')
    response_body = json.loads(response.get_data(as_text=True))
    expected_message = 'The method is not allowed for the requested URL.'

    assert response.status_code == 405
    assert response_body['status'] == 'Method Not Allowed'
    assert response_body['statusCode'] == 405
    assert response_body['errorMessage'] == expected_message
