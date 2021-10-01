from flask import Blueprint, render_template
from app.forms import LoginForm

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)
