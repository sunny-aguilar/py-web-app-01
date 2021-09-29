from flask import Flask

from .index.routes import index_bp


def create_app():
  app = Flask(__name__)

  with app.app_context():
    app.register_blueprint(index_bp)

  return app
