from dataclasses import dataclass

from app.configs.database import db


@dataclass
class GrupoDoisModel(db.Model):
    id: int
    nome: str
    idade: str
    conjuge: str

    __tablename__ = "grupo_dois"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    conjuge_id = db.Column(db.Integer, db.ForeignKey("grupo_um.id"))

    conjuge = db.relationship("GrupoUmModel", backref="conjuge", uselist=False)
