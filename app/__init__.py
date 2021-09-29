from flask import Flask

from .index.routes import index_bp
from .api.routes import api_bp


def create_app():
  app = Flask(__name__)

  with app.app_context():
    app.register_blueprint(index_bp)
    app.register_blueprint(api_bp)

  return app
