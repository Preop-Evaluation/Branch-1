# Medical Staff Model
class MedicalStaff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    roles = db.relationship('MedicalStaffRole', backref='staff', cascade="all, delete-orphan")