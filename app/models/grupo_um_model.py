from dataclasses import dataclass

from app.configs.database import db


@dataclass
class GrupoUmModel(db.Model):
    id: int
    nome: str
    idade: str

    __tablename__ = "grupo_um"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
