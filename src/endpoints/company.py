import json
from flask import request, Blueprint, Response

from src.models.company import Company
from src.utils.decorators import session, http_handling

company_bp = Blueprint('companies', __name__, url_prefix='/companies')


@company_bp.route('', methods=['GET'])
@http_handling
@session
def get_companies(context):
    companies = Company.get_companies(context)
    return Response(status=200, response=json.dumps(companies))


@company_bp.route('/<int:company_id>', methods=['GET'])
@http_handling
@session
def get_company(context, company_id):
    company = Company.get_company(context, company_id)
    return Response(status=200, response=json.dumps(company))


@company_bp.route('', methods=['POST'])
@http_handling
@session
def post_company(context):
    body = request.json
    Company.create_company(context, body)
    return Response(status=201, response="Company created successfully!")


@company_bp.route('/<int:company_id>', methods=['PUT'])
@http_handling
@session
def put_company(context, company_id):
    body = request.json
    Company.update_company(context, body, company_id)
    return Response(status=201, response="Company updated successfully")


@company_bp.route('/<int:company_id>', methods=['PATCH'])
@http_handling
@session
def patch_company(context, company_id):
    body = request.json
    Company.patch_company(context, body, company_id)
    return Response(status=201, response="Company patched successfully")


@company_bp.route('/<int:company_id>', methods=['DELETE'])
@http_handling
@session
def update_company(context, company_id):
    Company.delete_company(context, company_id)
    return Response(status=204, response="Company deleted successfully")
