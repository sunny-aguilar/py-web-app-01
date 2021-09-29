from flask import Blueprint, render_template

index_bp = Blueprint('index_bp', __name__, template_folder='templates')

@index_bp.route('/')
def index():
  msg = 'Index Page'
  return render_template('index.html', msg=msg)



