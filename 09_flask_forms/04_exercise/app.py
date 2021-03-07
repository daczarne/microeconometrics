from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (
	StringField,
	BooleanField,
	DateTimeField,
	RadioField,
	SelectField,
	TextField,
	TextAreaField,
	SubmitField
)
from wtforms.validators import DataRequired

# Instanciate the app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

# Define the class
class InfoForm(FlaskForm):
	breed = StringField("What breed are you?")
	submit = SubmitField("Submit")

# Index
@app.route("/", methods = ["GET", "POST"])
def index():
	# Create instance of the form.
	form = InfoForm()
	# If the form is filled-out get the breed and flash
	if form.validate_on_submit():
		session["breed"] = form.breed.data
		flash(f"You are a {session['breed']}")
		return redirect(url_for("index"))
	# Else, return the base html template
	return render_template("home.html", form = form)

# Run the app
if __name__ == "__main__":
	app.run(debug = True)
