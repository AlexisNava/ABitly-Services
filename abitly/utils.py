def format_exception(exception):
    """
    Handle the all the HTTPExceptions to return a tuple with the following
    values: statusCode, status, and error_message

    Parameters
    ----------

    exception : HTTPException
        The exception that catch the @app.errorhandler decorator

    Returns
    -------

    formatted_exception : tuple
        (statusCode: int, status: str, error_message: str)
    """

    # HTTPException Example:
    # 405 Method Not Allowed: The method is not allowed for the requested URL.

    # Create a list of strings from HTTPException splitted by :
    # ['405 Method Not Allowed',
    # 'The method is not allowed for the requested URL.']
    exception_list = str(exception).split(': ')

    # Get the statusCode from the slice of the first item of the exception_list
    statusCode = exception_list[0][:3]

    # Get the status from the slice of the first item of the exception_list
    status = exception_list[0][3:]

    # Get the error_message from the second item of the exception_list
    error_message = exception_list[1]

    return statusCode, status, error_message
