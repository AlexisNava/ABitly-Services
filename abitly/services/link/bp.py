"""Define the Blue Print for the Link Service"""

from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

# Controller
from flaskr.services.link.controller import (validate_request_body,
                                             get_generated_url)

link = Blueprint('link', __name__, url_prefix='/link')


@link.route('/', methods=['POST'])
def create_link():
    """Verifies if the original_url is already stored:
    - If not, creates a new generated_url and saves the original_url.
    - If yes, just returns the previously generated_url.

    Returns
    -------

    response : Response
        JSON response.

    Raises
    ------

    exception : HTTPException
        One of the HTTPExceptions.
    """

    try:
        # Validates the json format of the request
        original_url = validate_request_body(request.get_json())

        # Gets the saved generated_url or creates a new one
        generated_url = get_generated_url(original_url)

        return jsonify(statusCode=200, status='OK',
                       generated_url=generated_url
                       )

    except (BadRequest, InternalServerError) as error:
        raise error
