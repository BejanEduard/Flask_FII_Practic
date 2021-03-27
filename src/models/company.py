from sqlalchemy import Column, String, Integer

from src.adapters.company import CompanyAdapter
from src.models.base import Base
from src.utils.exceptions import Conflict
from src.utils.validators import validate_company_body

import json


class Company(Base, CompanyAdapter):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    street = Column(String(200))
    city = Column(String(100))
    country = Column(String(100))

    @classmethod
    def get_companies(cls, context):
        results = context.query(cls).all()
        return cls.to_json(results)

    @classmethod
    def get_company(cls, context, company_id):
        result = cls.get_company_by_id(context, company_id)
        return cls.to_single_json(result)

    @classmethod
    def create_company(cls, context, body):
        validate_company_body(body)

        company = Company()
        company.to_object(body)
        context.add(company)
        context.commit()

    @classmethod
    def update_company(cls, context, body, company_id):
        validate_company_body(body)

        company = cls.get_company_by_id(context, company_id)
        if not company:
            return Conflict("The company you are trying to update is missing", status=404)

        company.to_object(body)
        context.commit()

    @classmethod
    def delete_company(cls, context, company_id):
        company = cls.get_company_by_id(context,company_id)
        if not company:
            return Conflict("The company you are trying to delete does not exist!", status=404)

        context.delete(company)
        context.commit()


    @classmethod
    def get_company_by_id(cls, context, company_id):
        return context.query(cls).filter_by(id=company_id).first()
