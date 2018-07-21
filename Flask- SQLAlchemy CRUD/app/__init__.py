from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# config.py 설정파일
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'flasknotewithsqlalchemy'
db = SQLAlchemy(app)

from app import views, models
