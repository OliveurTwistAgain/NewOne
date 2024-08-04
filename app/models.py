# app/models.py

from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    # Optionnel: Ajouter une méthode pour représenter l'utilisateur
    def __repr__(self):
        return f'<User {self.username}>'

class PlaceToVisit(db.Model):
    __tablename__ = 'placestovisit'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Optionnel: Ajouter une méthode pour représenter le lieu
    def __repr__(self):
        return f'<PlaceToVisit {self.name}>'

class ContactUs(db.Model):
    __tablename__ = 'contactus'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)

    # Optionnel: Ajouter une méthode pour représenter le message
    def __repr__(self):
        return f'<ContactUs {self.name}>'
