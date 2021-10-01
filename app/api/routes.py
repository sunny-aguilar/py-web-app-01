from flask import Blueprint, render_template

api_bp = Blueprint('api_bp', __name__, template_folder='templates')

@api_bp.route('/api', methods=['GET', 'POST'])
def api():
  title = 'API Page'
  return render_template('api.html', title=title)
