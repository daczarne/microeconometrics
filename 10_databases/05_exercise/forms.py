from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# Add form
class AddForm(FlaskForm):
	name = StringField("Name of Puppy:")
	submit = SubmitField("Add Puppy")


# Owner
class AddOwnerForm(FlaskForm):
	name = StringField("Name of Owner:")
	pup_id = IntegerField("Id of Puppy:")
	submit = SubmitField("Add Owner")


# Delete form
class DelForm(FlaskForm):
	id = IntegerField("Id Number of Puppy to Remove:")
	submit = SubmitField("Remove Puppy")
