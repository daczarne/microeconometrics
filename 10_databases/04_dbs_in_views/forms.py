from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# Add form
class AddForm(FlaskForm):
	name = StringField("Name of Puppy:")
	submit = SubmitField("Add Puppy")

# Delete form
class DelForm(FlaskForm):
	id = IntegerField("Id Number of Puppy to Remove:")
	submit = SubmitField("Remove Puppy")
