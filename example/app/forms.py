from flask_wtf import FlaskForm
from wtforms import validators, TextAreaField, IntegerField, BooleanField, SubmitField

class MainForm(FlaskForm):
    text = TextAreaField(u'Text', [validators.DataRequired()])
    percentage = IntegerField(u'Percentage', [validators.DataRequired(),
                                              validators.NumberRange(min=0, max=100)])
    keywords_no = IntegerField(u'Keywords Number', [validators.DataRequired(),
                                                    validators.NumberRange(min=1)])
    rm_placeholders = BooleanField(u'Remove Placeholders')
