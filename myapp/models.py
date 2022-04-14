from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  calories = db.relationship('DailyCalories', backref='author', lazy=True)
  
  def __init__(self, email, username, password):
    self.email = email
    self.username = username
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  def __repr__(self):
    return f"Username {self.username}"

class DailyCalories(db.Model):
  __tablename__ = 'daily_calories'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  title = db.Column(db.String(300), nullable=False)
  breakfast = db.Column(db.String(600), nullable=False)
  breakfast_calories = db.Column(db.Integer, nullable=False)
  lunch = db.Column(db.String(600), nullable=False)
  lunch_calories = db.Column(db.Integer, nullable=False)
  dinner = db.Column(db.String(600), nullable=False)
  dinner_calories = db.Column(db.Integer, nullable=False)
  notes = db.Column(db.Text, nullable=False)


  def __init__(self, title, breakfast, lunch, dinner, notes, breakfast_calories, lunch_calories, dinner_calories, user_id):
    self.title = title
    self.breakfast = breakfast
    self.breakfast_calories = breakfast_calories
    self.lunch = lunch
    self.lunch_calories = lunch_calories
    self.dinner = dinner
    self.dinner_calories = dinner_calories
    self.notes = notes
    self.user_id = user_id
  
  def __repr__(self):
    return f"Post ID: {self.id} -- Date: {self.date} --- Title: {self.Title} -- Dinner: {self.dinner} -- Lunch: {self.lunch} -- Breakfast: {self.breakfast} -- Notes: {self.notes} -- Breakfast Calories: {self.breakfast_calories} -- Lunch Calories: {self.lunch_calories} -- Dinner Calories: {self.dinner_calories}"

