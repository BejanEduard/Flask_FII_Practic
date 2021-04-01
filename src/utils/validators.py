import re

from src.utils.exceptions import InvalidBody


def validate_user_body(body):
    validate_email(body["email"])
    validate_password(body["password"])


def validate_password(password):
    if not password:
        raise InvalidBody("You must provide a password", status=400)


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    result = re.search(regex, email)
    if not result:
        raise InvalidBody("Email address is not valid", status=400)


def validate_company_body(body):
    required_fields = ['name', 'street', 'city', 'country']
    for field in required_fields:
        if not body[field]:
            raise InvalidBody(f"Field <{field}>  is invalid", status=400)


def validate_company_assign(body):
    if not body['company_id'] or not body['user_id']:
        raise InvalidBody("Company or user missing.", status=400)
