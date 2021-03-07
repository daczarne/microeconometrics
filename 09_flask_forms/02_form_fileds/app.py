from flask import Flask, render_template, session, redirect, url_for, session
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


# Instalnciate the app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


# Build the form class
class InfoForm(FlaskForm):
	breed = StringField("What breed are you?", validators = [DataRequired()])
	neutered = BooleanField("Have you been neutered?")
	mood = RadioField(
		"Please choose your mood:",
		choices=[("mood_one", "Happy"), ("mood_two", "Excited")]
	)
	food_choice = SelectField(
		u"Pick your favorite food:",
		choices = [("chi", "Chicken"), ("bf", "Beef"), ("fish", "Fish")]
	)
	feedback = TextAreaField()
	submit = SubmitField("Submit")


# Index
@app.route("/", methods = ["GET", "POST"])
def index():
	# Initialize a form
	form = InfoForm()
	# Check if form has been submited at least once
	if form.validate_on_submit():
		# Get the input values
		session["breed"] = form.breed.data
		session["neutered"] = form.neutered.data
		session["mood"] = form.mood.data
		session["food"] = form.food_choice.data
		session["feedback"] = form.feedback.data
		# Redirect the user to the thankyou page
		return redirect(url_for("thankyou"))
	return render_template("home.html", form = form)


# Thank you
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")


# Run the app
if __name__ == "__main__":
	app.run(debug = True)
