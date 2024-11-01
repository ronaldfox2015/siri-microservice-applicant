from flask import Blueprint, current_app, request, jsonify

from app.applicant.application.input.user_input_dto import UserInputDTO
from app.applicant.application.services.user_service import UserService
from app.applicant.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
user_controller = Blueprint('user', __name__)
user_service = UserService(UserRepositoryImpl())


@user_controller.route('/health', methods=['GET'])
def verify_get():
    return jsonify(alive=True)


@user_controller.route('', methods=['POST'])
def create_user():
    data = request.get_json()  # Si se envían datos en JSON
    user_input = UserInputDTO(email=data["email"], password=data["password"], role=data["role"])
    user_input.set_confirm_password(data["confirm_password"])
    user = user_service.create_user(user_input)
    return jsonify({
        "code": 200*100,
        "message": "ok",
        "data": user
    }), 200


@user_controller.route('/auth/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    user_input = UserInputDTO(email=data["email"], password=data["password"], role=data["role"])
    user_input.set_confirm_password(data["password"])
    user = user_service.auth_login(user_input)
    if user:
        return jsonify(id=user.id, username=user.username)
    return jsonify(message='User not found'), 404
