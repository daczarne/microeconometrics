from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# Add puppy form
class AddForm(FlaskForm):
	name = StringField("Puppy name:")
	submit = SubmitField("Add puppy")

# Add owner form
class AddOwnerForm(FlaskForm):
	name = StringField("Name of owner:")
	pup_id = IntegerField("Id of Puppy:")
	submit = SubmitField("Add Owner")

# Delete form
class DelForm(FlaskForm):
	id = IntegerField("Id number of puppy to remove:")
	submit = SubmitField("Remove puppy")

