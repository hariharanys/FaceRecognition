from flask import (Blueprint,request,current_app,send_file,Response,jsonify)
from controller.testController import test_function
from controller.imageDetectionController import imageDetection

ds_blueprint = Blueprint('ds',__name__)

app = current_app

ds_blueprint.add_url_rule('/test-function',view_func=test_function,methods=['GET'])

ds_blueprint.add_url_rule('/image-detection',view_func=imageDetection,methods=['POST'])

