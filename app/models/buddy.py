from flask import current_app
from app import db

class Buddy(db.Model):
    buddy_id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    zipcode=db.Column(db.Text)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    morning =db.Column(db.Boolean)
    afternoon =db.Column(db.Boolean)
    evening =db.Column(db.Boolean)

    def to_json(self):
        return {
            'user_id': self.buddy_id,
            'zipcode': self.zipcode,
            'name': self.name,
            'email': self.email,
            'morning':self.morning,
            'afternoon':self.afternoon,
            'evening': self.evening
        }

