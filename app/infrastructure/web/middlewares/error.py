import logging
from flask import jsonify


class ErrorMiddleware:
    def __init__(self, app, **kwargs):
        self.logger = logging.getLogger("ErrorMiddleware")

        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app):
        @app.errorhandler(404)
        def not_found(error):
            return jsonify({"error": "Not Found", "message": str(error)}), 404

        @app.errorhandler(500)
        def internal_error(error):
            return (
                jsonify(
                    {
                        "error": "Internal Server Error",
                        "message": "An unexpected error occurred. Please try again later.",
                    }
                ),
                500,
            )

        @app.errorhandler(Exception)
        def handle_exception(error):
            return (
                jsonify({"error": error.__class__.__name__, "message": str(error)}),
                400,
            )
