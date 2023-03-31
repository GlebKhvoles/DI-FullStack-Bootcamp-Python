from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'robots.db')
app.config['SECRET_KEY']='123456'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes

# import json
# from app import models, db
# def populate():
# 	with open("./app/static/users.json", "r") as f:
# 		json_file = json.load(f)
# 	for json_person in json_file:
# 		user = models.User(name=json_person.get('name'), street=json_person.get('address').get('street'), city=json_person.get('address').get('city'), zipcode=json_person.get('address').get('zipcode'))
# 		db.session.add(user)
# 		db.session.commit()
#
# populate()