from flask import render_template, request, Blueprint
from myapp.models import DailyCalories

core = Blueprint('core', __name__)

@core.route('/')
def index():
  page = request.args.get('page', 1, type=int)
  daily_calories = DailyCalories.query.order_by(DailyCalories.date.desc()).paginate(page=page, per_page=5)
  return render_template('index.html', daily_calories=daily_calories)

@core.route('/info')
def info():
  return render_template('info.html')