from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///robocontrol.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SWAGGER"] = {
        "title": "RoboControl API",
        "uiversion": 3,
        "description": "API para gerenciamento de robôs, sensores e missões",
    }

    Swagger(app)

    db.init_app(app)

    from .routes import main

    app.register_blueprint(main)

    return app
