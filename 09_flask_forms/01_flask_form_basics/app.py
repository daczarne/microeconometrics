from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# Instanciate the app
app = Flask(__name__)

# Configure a secret SECRET_KEY
app.config["SECRET_KEY"] = "mysecretkey"

# Create the class
class InfoForm(FlaskForm):
	breed = StringField("What breed are you?")
	submit = SubmitField("Submit")

# Form
@app.route("/", methods = ["GET", "POST"])
def index():
	breed = False
	form = InfoForm()
	if form.validate_on_submit():
		breed = form.breed.data
		form.breed.data = ""
	return render_template("index.html", form = form, breed = breed)

# Run the app
if __name__ == "__main__":
	app.run(debug = True)
