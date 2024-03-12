from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy(app)

from app import routes, models
