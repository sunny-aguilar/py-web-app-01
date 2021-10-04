from flask import Blueprint, render_template, flash, redirect
from app.forms import LoginForm

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
    return redirect('/')
  return render_template('login.html', title='Sign In', form=form)
