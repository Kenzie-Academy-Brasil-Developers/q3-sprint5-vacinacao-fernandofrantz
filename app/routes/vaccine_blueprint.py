from flask import Blueprint
from app.controllers.vacinacao_controller import post_vaccine, get_vaccines

bp_vaccine = Blueprint('bp_vaccine', __name__, url_prefix='/api')

bp_vaccine.post('/vaccine')(post_vaccine)
bp_vaccine.get('/vaccine')(get_vaccines)
# bp_vaccine.patch('/vaccine')(get_vaccines)