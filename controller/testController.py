from flask import (jsonify,Response,request)
from middleware.errorHandling import ErrorHandling

def test_function():
    try:
        return jsonify({"message:successfully loaded"}),200
    except Exception as e:
       error_code = getattr(e,'code',500)
       error_message = str(e)
       return ErrorHandling.handle_error(error_code=error_code,error_message=error_message)