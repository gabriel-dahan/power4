from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_socketio import SocketIO

from dotenv import dotenv_values

CONF = dotenv_values('.env')

app = Flask(
    __name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates'
)
api = Api(app)
cors = CORS(app, resources = {r'/api/*': {'origins': '*'}})
socket = SocketIO(
    app, 
    path = '/websocket',
    cors_allowed_origins = ['http://127.0.0.1:5173']
)

app.url_map.strict_slashes = False

app.config['SECRET'] = CONF['SECRET']
app.config['BUNDLE_ERRORS'] = True

# --- DATABASE --- #
app.config['SQLALCHEMY_DATABASE_URI'] = CONF['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from src.resources import main, games, users