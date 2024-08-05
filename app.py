# app.py

# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run()

# app.py

from flask import Flask
from app import create_app

app = Flask(
    __name__,
    static_folder='static',  # Répertoire des fichiers statiques
    template_folder='app/templates'  # Répertoire des templates
)

if __name__ == "__main__":
    app.run()


