from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.grupo_um_model import GrupoUmModel 
    from app.models.grupo_dois_model import GrupoDoisModel