# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialisation des extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation des extensions avec l'application Flask
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configurez la fonction de chargement de l'utilisateur
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Importez User ici pour éviter les problèmes d'importation circulaire
        return User.query.get(int(user_id))

    # Importez les routes après la configuration de l'application
    from .views import main
    app.register_blueprint(main)

    return app
