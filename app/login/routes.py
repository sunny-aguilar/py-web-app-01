from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/login')
def login():
  form = LoginForm()
