from App.database import db
from datetime import datetime
import uuid

def generate_short_uuid():
    return str(uuid.uuid4())[:8]

class Questionnaire(db.Model):
    __tablename__ = 'questionnaire'
    id = db.Column(db.String(20), primary_key=True, default=generate_short_uuid, server_default='gen_random_uuid()')
    patient_id = db.Column(db.String(20), db.ForeignKey('patient.id'))
    responses = db.Column(db.JSON, nullable=True)  
    previous_responses = db.Column(db.JSON, nullable=True)  
    flagged_questions = db.Column(db.JSON, nullable=True)  
    operation_date = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(120), nullable=False, default='pending')
    evaluation_notes = db.Column(db.String(1200), nullable=True)
    anesthesiologist_notes = db.Column(db.String(1200), nullable=True)
    surgeon_notes = db.Column(db.String(1200), nullable=True)
    doctor_notes = db.Column(db.String(1200), nullable=True)
    submitted_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patient_id = kwargs.get('patient_id', None)
        self.responses = kwargs.get('responses', {})