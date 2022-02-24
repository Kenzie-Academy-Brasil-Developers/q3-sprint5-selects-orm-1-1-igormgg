from flask import jsonify
from sqlalchemy.orm import Query

from app.configs.database import db
from app.models.grupo_dois_model import GrupoDoisModel
from app.models.grupo_um_model import GrupoUmModel


def get_marriage():
    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .join(GrupoUmModel)
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data), 200


def get_by_limit(limite: int):
    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .join(GrupoUmModel)
        .limit(limite)
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data), 200


def get_by_first_char(caractere: str):
    char = caractere.upper()

    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .join(GrupoUmModel)
        .filter(GrupoDoisModel.nome.like(f"{char}%"))
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data), 200


def get_by_last_char(caractere: str):
    char = caractere.lower()

    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .join(GrupoUmModel)
        .filter(GrupoDoisModel.nome.like(f"%{char}"))
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data), 200


def get_by_age(idade: int):
    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .filter_by(idade=idade)
        .join(GrupoUmModel)
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data), 200


def get_by_id(id: int):
    group_query: Query = (
        db.session.query(GrupoDoisModel.nome, GrupoUmModel.nome)
        .select_from(GrupoDoisModel)
        .join(GrupoUmModel)
        .filter(GrupoDoisModel.id == id)
    )

    serialized_data = [
        {"nome": q[0], "conjuge": {"nome": q[1]}} for q in group_query.all()
    ]

    return jsonify(serialized_data[0]), 200
