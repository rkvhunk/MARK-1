import os
from flask import Flask, request
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# application = Flask(__name__)


app = None


def _create_app():
    app = Flask('my-service')
    return app

def _blueprint(app):
    from service import SERVICE
    # url_prefix = ''
    app.register_blueprint(SERVICE)
    return app

def _swagger(app):
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "My Service",
            "contact": {
                "hello":"world!"
            },
            "version": "1.0",
        },
    }
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'hello_world',
                "route": '/hello_world.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "",
        "swagger_ui": True,
        "specs_route": "/api/"
    }
    swagger = Swagger(app, template=swagger_template, config=swagger_config)
    return app

def _db(app):

    # from flask import Flask
    # from flask_sqlalchemy import SQLAlchemy
    # from flask_migrate import Migrate

    # app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    # class User(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     name = db.Column(db.String(128))

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/my_service'
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.secret_key = 'secret string'

    # db = SQLAlchemy(app)

    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/my-service"
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)

    # migrate = Migrate(app, db)
    # db.init_app(app)
    # migrate.init_app(app, db)

    # manager = Manager(app)
    # manager.add_command('db', MigrateCommand)
    return app

def _app():
    app = _create_app()
    app = _blueprint(app)
    app = _swagger(app)
    # app = _db(app)
    return app

def application():
    global app
    if app is None:
        app = _app()
        return app

application = application()