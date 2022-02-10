from flask import jsonify, request, current_app
from app.models.exc import CpfLengthError, JustAcceptStringError
from app.models.vacinacao_model import VacinacaoModel
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus


def post_vaccine():
    try:
        data = request.get_json()
        vaccine = VacinacaoModel(**data)

        current_app.db.session.add(vaccine)
        
        current_app.db.session.commit()
        return jsonify(vaccine.serializer()), HTTPStatus.CREATED

    except IntegrityError:
        return {"message": "You cannot add the same cpf two times, this one is probably already taken."}, HTTPStatus.CONFLICT

    except CpfLengthError as error:
        return {"message": str(error)}, HTTPStatus.BAD_REQUEST

    # except JustAcceptStringError as error:
    #     return {"message": str(error)}, HTTPStatus.BAD_REQUEST

def get_vaccines():
    vaccines = (VacinacaoModel.query.all())
    serializer = [
        {
            "cpf": vaccine.cpf,
            "name": vaccine.name,
            "first_shot_date": vaccine.first_shot_date,
            "second_shot_date": vaccine.second_shot_date,
            "vaccine_name": vaccine.vaccine_name,
            "health_unity_name": vaccine.health_unity_name
        } for vaccine in vaccines
    ]

    return {"vaccines": serializer}, HTTPStatus.OK
  
