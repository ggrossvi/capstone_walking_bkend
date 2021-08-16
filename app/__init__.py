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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://nngivouwherfmq:b52aa5022ea7c76da647445a1b10ee86113b4750f036ab1322cd73038e74a620@ec2-35-174-56-18.compute-1.amazonaws.com:5432/d66aoo1mughase'
    # 'postgresql+psycopg2://postgres@localhost:5432/walkingbuddy'
    
    

    db.init_app(app)
    migrate.init_app(app,db)

    from app.route import buddy_bp
    from app.models.buddy import Buddy
    app.register_blueprint(buddy_bp)
    
  
    return app
    