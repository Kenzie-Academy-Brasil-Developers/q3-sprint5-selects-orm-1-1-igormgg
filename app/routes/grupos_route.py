from flask import Blueprint

from app.controller.grupos_controller import (get_by_age, get_by_first_char,
                                              get_by_id, get_by_last_char,
                                              get_by_limit, get_marriage)

bp_grupos = Blueprint("bp_grupos", __name__, url_prefix="/grupos")

bp_grupos.get("")(get_marriage)
bp_grupos.get("/por_limite/<int:limite>")(get_by_limit)
bp_grupos.get("/inicia_pelo_caractere/<caractere>")(get_by_first_char)
bp_grupos.get("/termina_pelo_caractere/<caractere>")(get_by_last_char)
bp_grupos.get("/por_idade/<int:idade>")(get_by_age)
bp_grupos.get("/pelo_id/<int:id>")(get_by_id)
