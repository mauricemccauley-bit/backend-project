from .config import config_by_name
from .main import main_bp  
from flask import Flask
from .extensions import db, migrate

def create_app(config_name='development'):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])
    print("RUNTIME SECRET_KEY:", app.config["SECRET_KEY"])
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)

    return app