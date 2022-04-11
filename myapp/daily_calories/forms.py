from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DailyCaloriesForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  notes = TextAreaField('Text', validators=[DataRequired()])
  breakfast = StringField('Text', validators=[DataRequired()])
  lunch = StringField('Text', validators=[DataRequired()])
  dinner = StringField('Text', validators=[DataRequired()])
  submit = SubmitField('Post')