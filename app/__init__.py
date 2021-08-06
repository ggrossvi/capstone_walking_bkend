from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_sqlalchemy.model import camel_to_snake_case
# from flask import Blueprint
# from app import db
# from flask import request, Blueprint, make_response, jsonify
# from datetime import datetime
# import requests


db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config = None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql+psycopg2://postgres@localhost:5432/walkingbuddy'

    db.init_app(app)
    migrate.init_app(app,db)

    from .route import walking_buddy_bp
    app.register_blueprint(walking_buddy_bp)
    
    return app
    