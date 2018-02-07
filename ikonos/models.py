from datetime import datetime
from ikonos import db


class Enquiry(db.Model):
    __tablename__ = 'enquiries'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    message = db.Column(db.String())
    time_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, first_name, last_name, message):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.message = message

    def __repr__(self):
        return '<id {}>'.format(self.id)
