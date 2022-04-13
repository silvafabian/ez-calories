from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class DailyCaloriesForm(FlaskForm):
  title = StringField('Date', validators=[DataRequired()])
  notes = TextAreaField('Notes', validators=[DataRequired()])
  breakfast = StringField('Breakfast', validators=[DataRequired()])
  breakfast_calories = IntegerField('Breakfast Calories', validators=[DataRequired()])
  lunch = StringField('Lunch', validators=[DataRequired()])
  lunch_calories = IntegerField('Lunch Calories', validators=[DataRequired()])
  dinner = StringField('Dinner', validators=[DataRequired()])
  dinner_calories = IntegerField('Dinner Calories', validators=[DataRequired()])
  submit = SubmitField('Post')