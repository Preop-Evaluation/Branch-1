from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def get_migrate(app):
    return Migrate(app, db)

def init_db(app):
    db.init_app(app)

def create_db():
    db.create_all()
    
