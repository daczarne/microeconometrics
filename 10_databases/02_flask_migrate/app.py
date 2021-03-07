import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Get the file path to the app
basedir = os.path.abspath(os.path.dirname(__file__))

# Instanciate the app
app = Flask(__name__)

# Config the DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Connect app and DB
Migrate(app,db)

# Define the item class
class Puppy(db.Model):
	# Set table name
	__tablename__ = "puppies"

	# Define table schema
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	age = db.Column(db.Integer)
	breed = db.Column(db.Text)
	
	# Item constructor
	def __init__(self, name, age, breed):
		self.name = name
		self.age = age
		self.breed = breed

	# Item repr 
	def __repr__(self):
		return f"Puppy {self.name} is {self.age} years old."
