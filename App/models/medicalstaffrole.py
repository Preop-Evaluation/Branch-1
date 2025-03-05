# Medical Staff Role Model
class MedicalStaffRole(db.Model):
    staff_id = db.Column(db.Integer, db.ForeignKey('medical_staff.staff_id'), primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('medical_role.type_id'), primary_key=True)
    role = db.relationship('MedicalRole', backref='staff_roles')