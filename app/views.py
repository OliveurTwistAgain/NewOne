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
