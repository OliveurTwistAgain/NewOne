# populate_db.py

from app import create_app, db
from app.models import User, PlaceToVisit, ContactUs

app = create_app()

with app.app_context():
    db.create_all()

    # Ajouter des utilisateurs
    user1 = User(username='alice', email='alice@example.com', password='password123')
    user2 = User(username='bob', email='bob@example.com', password='password456')
    db.session.add(user1)
    db.session.add(user2)

    # Ajouter des lieux à visiter
    place1 = PlaceToVisit(name='Eiffel Tower', description='Iconic Parisian landmark')
    place2 = PlaceToVisit(name='Louvre Museum', description='World-famous art museum')
    db.session.add(place1)
    db.session.add(place2)

    # Ajouter des messages de contact
    contact1 = ContactUs(name='Charlie', email='charlie@example.com', message='Hello!')
    db.session.add(contact1)

    db.session.commit()
