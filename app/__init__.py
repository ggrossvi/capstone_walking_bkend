from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_sqlalchemy.model import camel_to_snake_case
# from flask import Blueprint
# from app import db
# from flask import request, Blueprint, make_response, jsonify
# from datetime import datetime
#import requests
from dotenv import load_dotenv
import os



db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config = None):
    app = Flask(__name__)
    # allows localhost access
    CORS(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    

    db.init_app(app)
    migrate.init_app(app,db)

    from app.route import buddy_bp
    from app.models.buddy import Buddy
    app.register_blueprint(buddy_bp)
    
  
    return app
    