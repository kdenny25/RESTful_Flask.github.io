# RESTful_flask/my_app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Tallguy63!!@localhost:5433/debug"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)

db.create_all()

from my_app.product.views import comment_list
app.register_blueprint(comment_list)