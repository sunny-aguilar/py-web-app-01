from flask import Blueprint, render_template

index_bp = Blueprint('index_bp', __name__, template_folder='templates')

@index_bp.route('/')
@index_bp.route('/index')
def index():
  """ 2nd decorators adds another route to same function """
  user = {'username': 'Sandro', }
  posts = [
    {
      'author': {'username': 'Olly'},
      'body': 'Rivers of Norcal'
    },
    {
      'author': {'username': 'Misterie'},
      'body': 'Camping and Hicking Tips'
    }]
  msg = 'Index Page'
  title = 'Index Page'
  return render_template('index.html', msg=msg, title=title)



