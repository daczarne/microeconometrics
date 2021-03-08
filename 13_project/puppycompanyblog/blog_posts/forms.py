from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Blog Post Form
class BlogPostForm(FlaskForm):
	title = StringField("Title", validators = [DataRequired()])
	text = TextAreaField("Text", validators = [DataRequired()])
	submit = SubmitField("BlogPost")
