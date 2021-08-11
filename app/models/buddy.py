from flask import current_app
from app import db

class Buddy(db.Model):
    buddy_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    address=db.Column(db.Text)
    apt=db.Column(db.Text)
    city=db.Column(db.Text)
    state=db.Column(db.Text)
    zipcode=db.Column(db.Text)
    email = db.Column(db.Text)
    morning =db.Column(db.Boolean)
    afternoon =db.Column(db.Boolean)
    evening =db.Column(db.Boolean)

    def to_json(self):
        return {
            'buddy_id': self.buddy_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'apt': self.apt,
            'city':self.city,
            'state':self.state,
            'zipcode': self.zipcode,
            'email': self.email,
            'morning':self.morning,
            'afternoon':self.afternoon,
            'evening': self.evening
        }

