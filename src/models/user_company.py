from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from src.adapters.user_company import UserCompanyAdapter
from src.models.base import Base
from src.utils.exceptions import Conflict, HTTPException
from src.utils.validators import validate_company_assign


class UserCompany(Base, UserCompanyAdapter):
    __tablename__ = 'user_company'
    __table_args__ = (PrimaryKeyConstraint('user_id', 'company_id'),)

    user_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    company_id = Column(Integer, ForeignKey("company.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    @classmethod
    def get_company_by_id(cls, context, company_id):
        results = context.query(cls).filter_by(company_id=company_id).all()
        return cls.to_json(results)

    @classmethod
    def get_user_company(cls, context, company_id, user_id):
        result = context.query(cls).filter_by(company_id=company_id, user_id=user_id).first()
        return result



    @classmethod
    def assign_user_to_company(cls, context, company_id, body):
        body['company_id'] = company_id
        validate_company_assign(body)
        if cls.get_user_company(context, company_id, body['user_id']):
            raise Conflict("Assignment already exists!", status=409)

        user_company = UserCompany()
        user_company.to_object(body)
        context.add(user_company)
        context.commit()

    @classmethod
    def delete_user_company(cls, context, company_id, user_id):
        user_company = cls.get_user_company(context, company_id, user_id)
        if not user_company:
            raise HTTPException("User's company not found", status=404)

        context.delete(user_company)
        context.commit()


