from flask import (jsonify)

class ErrorHandling:
    @staticmethod
    def handle_error(error_code,error_message=None):
        error_handlers = {
            400: ErrorHandling.bad_request,
            404: ErrorHandling.not_found,
            500: ErrorHandling.internal_server_error,
            501: ErrorHandling.default_error
        }
        error_handler = error_handlers.get(error_code,ErrorHandling.default_error)

        return error_handler(error_message)
    
    @staticmethod
    def bad_request(error_message = None):
        return jsonify({"error":error_message or "Bad Request"}),400
    
    @staticmethod
    def not_found(error_message = None):
        return jsonify({"error":error_message or "Resource not found"}),404
    
    @staticmethod
    def internal_server_error(error_message = None):
        return jsonify({"error":error_message or "Internal Server Error"}),500
    
    @staticmethod
    def default_error(error_message = None):
        return jsonify({"error":error_message or "Unknown Error"}),501