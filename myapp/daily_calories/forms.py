from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class DailyCaloriesForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  notes = TextAreaField('Text', validators=[DataRequired()])
  breakfast = StringField('Breakfast', validators=[DataRequired()])
  lunch = StringField('Lunch', validators=[DataRequired()])
  dinner = StringField('Dinner', validators=[DataRequired()])
  submit = SubmitField('Post')