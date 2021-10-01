from flask import Blueprint, render_template

api_bp = Blueprint('api_bp', __name__, template_folder='templates')

@api_bp.route('/api')
def api():
  msg = 'API Page'
  title = 'Index Page'
  return render_template('api.html', msg=msg, title=title)
