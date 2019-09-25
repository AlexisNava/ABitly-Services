from werkzeug.exceptions import MethodNotAllowed

# Utils
from abitly.utils import format_exception


def test_format_exception_should_format_method_not_allowed():
    """Should format the MethodNotAllowed Exception"""
    exception = MethodNotAllowed()
    statusCode, status, error_message = format_exception(exception)

    assert statusCode == 405
    assert status == 'Method Not Allowed'
    assert error_message == 'The method is not allowed for the requested URL.'
