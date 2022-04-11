from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp import daily_calories 
from myapp.models import DailyCalories
from myapp.daily_calories.forms import DailyCaloriesForm

daily_calories = Blueprint('daily_calories', __name__)

@daily_calories.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
  form = DailyCaloriesForm()
  if form.validate_on_submit():
    daily_calories = DailyCalories(
      title=form.title.data, 
      text=form.text.data, 
      user_id=current_user.id,
      breakfast=form.string.data,
      lunch=form.string.data,
      dinner=form.string.data
    )
    db.session.add(daily_calories)
    db.session.commit()
    flash('Calories was Created')
    print('Calorie post was created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)