from flask_login import UserMixin
from App.database import db
import uuid

class MedicalRole(db.Model, UserMixin):
    __abstract__ = True
    __tablename__ = 'MedicalRole'
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50), unique=True, nullable=False)