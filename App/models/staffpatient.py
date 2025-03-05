# Staff-Patient Relationship Model
class StaffPatient(db.Model):
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'), primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('medical_staff.staff_id'), primary_key=True)