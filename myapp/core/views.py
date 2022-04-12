from re import U
from flask import render_template, request, Blueprint
from flask_login import current_user
from myapp.models import DailyCalories, User

core = Blueprint('core', __name__)

@core.route('/')
def index():
  page = request.args.get('page', 1, type=int)
  daily_calories = DailyCalories.query.order_by(DailyCalories.date.desc()).paginate(page=page, per_page=5)
  user = User
  return render_template('index.html', daily_calories=daily_calories, current_user=current_user, user=user)
