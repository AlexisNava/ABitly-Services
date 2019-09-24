from werkzeug.exceptions import MethodNotAllowed

# Utils
from abitly.utils import format_exception


def test_format_method_not_allowed_exception():
    """Should format the MethodNotAllowed Exception"""
    exception = MethodNotAllowed()
    statusCode, status, error_message = format_exception(exception)

    assert statusCode == 405
    assert status == 'Method Not Allowed'
    assert statusCode == 'The method is not allowed for the requested URL.'
