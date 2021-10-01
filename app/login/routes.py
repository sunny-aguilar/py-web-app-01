from flask import Blueprint, render_template
from app import app
from app.forms import LoginForm

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

@login_bp.route('/login')
def login():
  form = LoginForm()
