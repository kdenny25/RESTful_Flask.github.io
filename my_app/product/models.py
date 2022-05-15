# RESTful_flask/my_app/product/models.py

from my_app import db
from datetime import date, datetime



class Contact_Us(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    #date = db.Column(db.Date)

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment
        #self.date = datetime.now().date()

    def __repr__(self):
        return '<Contact_Us %d>' % self.id