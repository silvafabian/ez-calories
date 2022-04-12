from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import DailyCalories
from myapp.daily_calories.forms import DailyCaloriesForm

daily_calories = Blueprint('daily_calories', __name__)

@daily_calories.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
  form = DailyCaloriesForm()
  if form.validate_on_submit():
    daily_calorie = DailyCalories(
      title=form.title.data, 
      user_id=current_user.id,
      breakfast=form.breakfast.data,
      breakfast_calories=form.breakfast_calories.data,
      lunch=form.lunch.data,
      lunch_calories=form.lunch_calories.data,
      dinner=form.dinner.data,
      dinner_calories=form.dinner_calories.data,
      notes=form.notes.data
    )
    db.session.add(daily_calorie)
    db.session.commit()
    flash('Calories was Created')
    print('Calories post was created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)

@daily_calories.route('/<int:daily_calories_id>')
def daily_calorie(daily_calories_id):
  daily_calories = DailyCalories.query.get_or_404(daily_calories_id) 
  return render_template(
    'daily_calories.html', 
    title=daily_calories.title, 
    date=daily_calories.date,
    breakfast=daily_calories.breakfast, 
    breakfast_calories=daily_calories.breakfast_calories, 
    lunch=daily_calories.lunch,
    lunch_calories=daily_calories.lunch_calories, 
    dinner=daily_calories.dinner, 
    dinner_calories=daily_calories.dinner_calories, 
    notes=daily_calories.notes, 
    post=daily_calories
  )

@daily_calories.route('/<int:daily_calories_id>/update',methods=['GET','POST'])
@login_required
def update(daily_calorie_id):
  daily_calorie = DailyCalories.query.get_or_404(daily_calorie_id)

  if daily_calorie.author != current_user:
    abort(403)

  form = DailyCaloriesForm()

  if form.validate_on_submit():
    daily_calorie.title = form.title.data
    daily_calorie.breakfast = form.breakfast.data
    daily_calorie.breakfast_calorie = form.breakfast_calorie.data
    daily_calorie.lunch = form.lunch.data
    daily_calorie.lunch_calorie = form.lunch_calorie.data
    daily_calorie.dinner = form.dinner.data
    daily_calorie.dinner_calorie = form.dinner_calorie.data
    daily_calorie.notes = form.notes.data
    db.session.commit()
    flash('Calories Updated')
    return redirect(url_for('daily_calories.daily_calorie',daily_calorie_id=daily_calorie.id))

  elif request.method == 'GET':
    form.title.data = daily_calorie.title
    form.note.data = daily_calorie.notes
    form.breakfast.data = daily_calorie.breakfast
    form.breakfast_calorie.data = daily_calorie.breakfast_calorie
    form.lunch.data = daily_calorie.lunch
    form.lunch_calorie.data = daily_calorie.lunch_calorie
    form.dinner.data = daily_calorie.dinner
    form.dinner_calorie.data = daily_calorie.dinner_calorie

  return render_template('create_post.html',title='Updating Calories',form=form)

@daily_calories.route('/<int:daily_calories_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(daily_calorie_id):
  daily_calorie = DailyCalories.query.get_or_404(daily_calorie_id)
  if daily_calorie.author != current_user:
    abort(403)
  db.session.delete(daily_calorie)
  db.session.commit()
  flash('Calories Deleted')
  return redirect(url_for('core.index'))