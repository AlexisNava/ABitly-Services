"""Define App Factory function to create the Flask App"""

import os
from flask import Flask, jsonify


def create_app():
    """Configure the Flask App"""

    app = Flask(__name__, instance_relative_config=True)

    # Routes
    @app.route('/')
    def index():
        message_text = 'Flaskr is running on'
        message_url = f'http://{os.getenv("HOST")}:{os.getenv("PORT")}'

        return jsonify(statusCode=200,
                       status='OK',
                       message=f'{message_text} {message_url}')

    # Error Handlers
    @app.errorhandler(400)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def method_not_allowed(exception):
        exception_list = str(exception).split(': ')
        statusCode = exception_list[0][:3]
        status = exception_list[0][3:]
        error_message = exception_list[1]

        return jsonify(statusCode=statusCode,
                       status=status,
                       errorMessage=error_message
                       ), statusCode

    return app
