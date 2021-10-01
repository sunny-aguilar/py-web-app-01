from flask import Flask
from config import Config

from .index.routes import index_bp
from .api.routes import api_bp
from .login.routes import login_bp


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  with app.app_context():
    app.register_blueprint(index_bp)
    app.register_blueprint(api_bp)

  return app
