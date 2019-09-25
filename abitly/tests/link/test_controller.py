import pytest
from werkzeug.exceptions import BadRequest

# Link Controller
from abitly.services.link.controller import validate_request_body


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
