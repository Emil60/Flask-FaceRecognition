from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Text



app = Flask(__name__)
app.config['SECRET_KEY']="something"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbase.db'
app.config['IMAGE_UPLOADS'] = '~/Desktop/Flask/flsk_faceapp/flskfaceapp/photos'
app.config['IMAGE_UPLOADS_TEMP'] = './flskfaceapp/temp'
db = SQLAlchemy(app)
from flskfaceapp import routes