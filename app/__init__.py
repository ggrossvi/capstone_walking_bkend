from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config = None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql+psycopg2://postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app,db)

    from .route import hello_world_bp
    app.register_blueprint(hello_world_bp)
    
    return  app
    