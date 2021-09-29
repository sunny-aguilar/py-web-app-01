from flask import Flask
from flask.blueprints import Blueprint

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
  return '<h1>Index Page<h1>'
