import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Get directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Instanciate the app and set the DB
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Define model class for puppies
class Puppy(db.Model):

	# Table name
	__tablename__ = "puppies"

	# Define the table schema
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	# One puppy -> many toys
	toys = db.relationship("Toy", backref = "puppy", lazy = "dynamic")
	# One puppy -> one owner
	owner = db.relationship("Owner", backref = "puppy", uselist = False)

	# Constructor
	def __init__(self, name):
		self.name = name

	# Repr
	def __repr__(self):
		if self.owner:
			return f"Puppy name is {self.name} and owner is {self.owner.name}"
		else:
			return f"Puppy name is {self.name} and has no owner assigned yet!"

	# Toys
	def report_toys(self):
		print("Here are my toys!")
		for toy in self.toys:
			print(toy.item_name)


# Build model for toys
class Toy(db.Model):

	# Table name
	__tablename__ = "toys"

	# Schema
	id = db.Column(db.Integer, primary_key = True)
	item_name = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

	# Constructor
	def __init__(self, item_name, puppy_id):
		self.item_name = item_name
		self.puppy_id = puppy_id


# Owners class
class Owner(db.Model):

	# Table name
	__tablename__ = "owners"

	# Schema
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

	# Constructor
	def __init__(self, name, puppy_id):
		self.name = name
		self.puppy_id = puppy_id
