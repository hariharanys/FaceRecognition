from flask import Flask
from apiflask import APIFlask
from routes.routes import ds_blueprint
from flask_cors import CORS
from dotenv import load_dotenv
import os

dot_env_path = './.env'

load_dotenv(dot_env_path)

app =Flask(__name__)

CORS(app, resources={r"/face-recognization/*": {"origins": "*"}})
app.register_blueprint(ds_blueprint, url_prefix = '/face-recognization')

if __name__ == '__main__':
    app.run(host=os.getenv('FLAS_HOST'), port=os.getenv('FLASK_RUN_PORT'),debug=True)