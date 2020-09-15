
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../src"))

flask = Flask(__name__)
flask.config.from_pyfile('config.py')

db = SQLAlchemy(flask)
with flask.app_context():
    db.create_all()
#flask.register_blueprint(webcontroller)
