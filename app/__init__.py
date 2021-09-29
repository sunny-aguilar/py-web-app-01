from flask import Flask

from app.index import index_bp


def create_app():
  app = Flask(__name__)

  return app
