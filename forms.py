from typing_extensions import Required
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class ContactForm(FlaskForm):
    contact_name = StringField("Contact Name:")
    contact_email = StringField("Contact Email:")
    message_content = TextAreaField("Question or Query:")
    submit = SubmitField("Submit Request")