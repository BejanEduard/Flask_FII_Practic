import json
from flask import request, Blueprint, Response

from src.models.company import Company
from src.models.user_company import UserCompany
from src.utils.decorators import session, http_handling, is_authorized, is_admin

company_bp = Blueprint('companies', __name__, url_prefix='/companies')


@company_bp.route('', methods=['GET'])
@http_handling
@session
@is_authorized
def get_companies(context, user):
    companies = Company.get_companies(context)
    return Response(content_type="application/json", status=200, response=json.dumps(companies))


@company_bp.route('/<int:company_id>', methods=['GET'])
@http_handling
@session
@is_authorized
def get_company(context, company_id, user):
    company = Company.get_company(context, company_id)
    return Response(content_type="application/json",status=200, response=json.dumps(company))


@company_bp.route('', methods=['POST'])
@http_handling
@session
@is_authorized
@is_admin
def post_company(context, user):
    body = request.json
    Company.create_company(context, body)
    return Response(status=201, response="Company created successfully!")


@company_bp.route('/<int:company_id>', methods=['PUT'])
@http_handling
@session
@is_authorized
@is_admin
def put_company(context, company_id, user):
    body = request.json
    Company.update_company(context, body, company_id)
    return Response(status=201, response="Company updated successfully")


@company_bp.route('/<int:company_id>', methods=['PATCH'])
@http_handling
@session
@is_authorized
@is_admin
def patch_company(context, company_id, user):
    body = request.json
    Company.patch_company(context, body, company_id)
    return Response( status=201, response="Company patched successfully")


@company_bp.route('/<int:company_id>', methods=['DELETE'])
@http_handling
@session
@is_authorized
@is_admin
def delete_company(context, company_id, user):
    Company.delete_company(context, company_id)
    return Response(status=204, response="Company deleted successfully")


@company_bp.route('/<int:company_id>/assign', methods=['POST'])
@http_handling
@session
@is_authorized
@is_admin
def assign_user_to_company(context, company_id, user):
    body = request.json
    UserCompany.assign_user_to_company(context, company_id, body)
    return Response(status=201, response="Assignment done successfully")


@company_bp.route('/<int:company_id>/users', methods=['GET'])
@http_handling
@session
@is_authorized
@is_admin
def get_company_users(context, company_id, user):
    results = UserCompany.get_company_by_id(context, company_id)
    return Response(content_type="application/json", status=200, response=json.dumps(results))


@company_bp.route('/<int:company_id>/users/<int:user_id>', methods=['DELETE'])
@http_handling
@session
@is_authorized
@is_admin
def delete_company_user(context, company_id, user_id, user):
    UserCompany.delete_user_company(context, company_id, user_id)
    return Response(status=200, response="User's company deleted successfully")
