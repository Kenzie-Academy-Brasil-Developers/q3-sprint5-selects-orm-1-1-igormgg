from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.grupo_dois_model import GrupoDoisModel
    from app.models.grupo_um_model import GrupoUmModel
