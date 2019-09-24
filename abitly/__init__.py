"""Define App Factory function to create the Flask App"""

import os
from flask import Flask, jsonify

# Configuration
from abitly.config import ProductionConfig, TestingConfig, DevelopmentConfig

# Utils
from abitly.utils import format_exception


def create_app():
    """Configure the Flask App"""

    app = Flask(__name__, instance_relative_config=True)
    flask_env = os.getenv('FLASK_ENV')

    # Use Config Classes per FLASK_ENV
    if flask_env == 'production':
        app.config.from_object(ProductionConfig)
    elif flask_env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

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
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def method_not_allowed(exception):
        statusCode, status, error_message = format_exception(exception)

        return jsonify(statusCode=statusCode,
                       status=status,
                       errorMessage=error_message
                       ), statusCode

    return app
