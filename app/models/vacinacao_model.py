from datetime import timedelta, date
from sqlalchemy.orm import validates
from sqlalchemy import Column, String, Date
from app.configs.database import db
from app.models.exc import CpfLengthError, JustAcceptStringError, InvalidFieldsError

class VacinacaoModel(db.Model):
    __tablename__ = "vaccine_cards"

    cpf: str = Column(String, primary_key=True)
    name: str = Column(String, nullable=False)
    first_shot_date: str = Column(Date, default=date.today())
    second_shot_date: str = Column(Date, default=date.today() + timedelta(days=90))
    vaccine_name: str = Column(String, nullable=False)
    health_unity_name: str = Column(String)

    def serializer(self):
        return {
            "cpf": self.cpf,
            "name": self.name,
            "first_shot_date": self.first_shot_date,
            "second_shot_date": self.second_shot_date,
            "vaccine_name": self.vaccine_name,
            "health_unity_name": self.health_unity_name
        }

    @validates("cpf")
    def validate_cpf_length(self, key, cpf):
        if (len(cpf) != 11):
            raise CpfLengthError("Cpf should contain 11 characters")
        return cpf

    # @validates("cpf", "name", "vaccine_name", "health_unity_name")
    # def validate_string_fields(self, key, cpf, name, vaccine_name, health_unity_name):
    #     if(
    #         type(cpf) != str or
    #         type(name) != str or
    #         type(vaccine_name) != str or
    #         type(health_unity_name) != str
    #     ):
    #         raise JustAcceptStringError("You cannot send any data that is not string")
    #     return self

    # @validates("cpf", "name", "vaccine_name", "health_unity_name")
    # def validate_keys(self, key, cpf, name, vaccine_name, health_unity_name):
    #     if(
    #         cpf == None or
    #         name == None or
    #         vaccine_name == None or
    #         health_unity_name == None
    #     ):
    #         raise InvalidFieldsError("Invalid key or keys, the valid ones are: cpf, name, vaccine_name, health_unity_name")