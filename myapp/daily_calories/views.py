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
      dinner=form.string.data,
      notes=form.string.data
    )
    db.session.add(daily_calories)
    db.session.commit()
    flash('Calories was Created')
    print('Calorie post was created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)

@daily_calories.route('/<int:daily_calories_id>')
def daily_calories(daily_calories_id):
  daily_calories = DailyCalories.query.get_or_404(daily_calories_id) 
  return render_template(
    'daily_calories.html', 
    title=daily_calories.title, 
    date=daily_calories.date,
    breakfast=daily_calories.breakfast, 
    lunch=daily_calories.lunch,
    dinner=daily_calories.dinner, 
    notes=daily_calories.notes, 
    post=daily_calories
  )

@daily_calories.route('/<int:daily_calorie_id>/update',methods=['GET','POST'])
@login_required
def update(daily_calorie_id):
  daily_calorie = DailyCalories.query.get_or_404(daily_calorie_id)
  if daily_calorie.author != current_user:
    abort(403)
  form = DailyCaloriesForm()
  if form.validate_on_submit():
    daily_calorie.title = form.title.data
    daily_calorie.text = form.text.data
    daily_calorie.breakfast = form.string.data
    daily_calorie.lunch = form.string.data
    daily_calorie.dinner = form.string.data
    daily_calorie.notes = form.text.data
    db.session.commit()
    flash('Calories Updated')
    return redirect(url_for('daily_calories.daily_calorie',daily_calorie_id=daily_calorie.id))
  elif request.method == 'GET':
    form.title.data = daily_calorie.title
    form.text.data = daily_calorie.text
    form.text.data = daily_calorie.notes
    form.string.data = daily_calorie.breakfast
    form.string.data = daily_calorie.lunch
    form.string.data = daily_calorie.dinner

  return render_template('create_post.html',title='Updating Calories',form=form)