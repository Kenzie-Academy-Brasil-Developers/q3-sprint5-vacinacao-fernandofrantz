from flask import Flask
from app.routes.vaccine_blueprint import bp_vaccine

def init_app(app: Flask):
    app.register_blueprint(bp_vaccine)