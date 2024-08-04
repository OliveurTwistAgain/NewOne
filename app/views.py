# app/views.py

from flask import Blueprint, render_template, request
from app import db
from app.models import PlaceToVisit
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Récupérer les 3 derniers lieux ajoutés
    latest_places = PlaceToVisit.query.order_by(PlaceToVisit.id.desc()).limit(3).all()
    return render_template('index.html', latest_places=latest_places)

@main.route('/search', methods=['GET', 'POST'])
def search():
    places = []
    if request.method == 'POST':
        # Récupérer la position entrée par l'utilisateur
        location = request.form.get('location')
        # Pour simplifier, on suppose que `location` correspond au nom d'un lieu dans la base de données
        # En pratique, tu devras utiliser une API de géocodage pour obtenir des coordonnées
        places = PlaceToVisit.query.filter(PlaceToVisit.name.ilike(f'%{location}%')).limit(5).all()
    
    return render_template('index.html', places=places)

