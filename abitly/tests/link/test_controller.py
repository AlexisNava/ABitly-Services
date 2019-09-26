import pytest
from werkzeug.exceptions import BadRequest, InternalServerError

# Link Controller
from abitly.services.link.controller import (validate_request_body,
                                             get_generated_url)


def test_validate_request_body_should_return_original_url():
    """Should return the original url when it is in the request body
    and it is of type str
    """

    request_data = {'originalUrl': 'https://realpython.com/'}
    expected_original_url = 'https://realpython.com/'

    original_url = validate_request_body(request_data)

    assert original_url == expected_original_url


def test_validate_request_body_should_raise_bad_request():
    """Should raise BadRequest exception when the originalUrl is not in the
    request body or it is of another type of string
    """

    request_data_empty = {}
    request_data_wrong_type = {'originalUrl': 10}

    with pytest.raises(BadRequest):
        validate_request_body(request_data_empty)

    with pytest.raises(BadRequest):
        validate_request_body(request_data_wrong_type)


def test_get_generated_url_should_return_generated_url():
    """Should return the generated url when the
    original_url is of type str
    """

    original_url = 'https://circleci.com/'
    generated_url = get_generated_url(original_url)

    assert len(generated_url) == 7


def test_get_generated_url_should_raise_internal_server_error():
    """Should raise InternalServerError when the
    original_url is another of type str
    """

    original_url = 10

    with pytest.raises(InternalServerError):
        get_generated_url(original_url)
