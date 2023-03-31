from flask import Response, request, make_response
from flask_restful import Resource
from users.service import (
    create_user,
    reset_passwrod_email_send,
    login_user,
    reset_password,
)


class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = reset_passwrod_email_send(request, input_data)
        return make_response(response, status)


class ResetPassword(Resource):
    @staticmethod
    def post(token) -> Response:
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)
