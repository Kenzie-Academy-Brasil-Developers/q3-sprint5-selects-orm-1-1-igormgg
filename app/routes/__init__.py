from flask import Flask

from app.routes.grupos_route import bp_grupos


def init_app(app: Flask):
    app.register_blueprint(bp_grupos)
