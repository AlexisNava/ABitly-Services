"""Define process functions to use in the Link Service"""

from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from shortuuid import ShortUUID

# DataBase
from abitly.db import db_session

# Models
from abitly.models import Link


def validate_request_body(body):
    """Validates the json format of the request

    Parameters
    ----------

    body : dict
        A JSON object with the originalUrl property:
        '{ originalUrl: "https://realpython.com/" }'

    Raises
    ------

    exception : BadRequest
        Raises a BadRequest exception when the originalUrl is not
    found in the JSON object or if it is not of type str

    Returns
    -------

    originalUrl : str
        Returns the received originalUrl.
    """

    if 'originalUrl' not in body or type(body['originalUrl']) != str:
        raise BadRequest
    else:
        return body['originalUrl']


def get_generated_url(original_url):
    """Gets the saved generated_url or creates a new one

    Parameters
    ----------

    original_url : str
        Verified original_url

    Raises
    ------

    exception : InternalServerError
        Raises an InternalServerError exception when catching an unexpected
    error

    Returns
    -------

    generated_url : str
        The new or the previously saved generated_url
    """

    try:
        # Search in the links table the original_url
        found_original_url = Link.query.filter(Link.original_url ==
                                               original_url).first()

        # If finds a saved original_url returns it
        if found_original_url:
            return found_original_url.generated_url

        # Create a new generated_url
        generated_url = ShortUUID().random(length=7)

        # Create a new Link
        link = Link(original_url, generated_url)

        # Saves the new link
        db_session.add(link)
        db_session.commit()

        return generated_url

    except Exception:
        raise InternalServerError


def get_original_url(generated_url):
    """Get the original_url

    Parameters
    ----------

    generated_url : str
        Saved generated_url

    Raises
    ------

    exception : BadRequest
        Raises BadRequest when the generated_url is not a string or is a string
    with a minor length to 7

    exception : NotFound
        Raises NotFound when the generated_url is valid but is not found
    in the links table

    Returns
    -------

    found_original_url : str
        The saved original_url
    """
    if type(generated_url) == str and len(generated_url) == 7:
        # Search the original url by the generated_url
        found_original_url = Link.query.filter_by(
            generated_url=generated_url).first()

        if found_original_url:
            return found_original_url.original_url

        raise NotFound

    raise BadRequest
