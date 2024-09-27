from flask import Blueprint, request, jsonify
from app.application.services.user_service import UserService
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl

user_bp = Blueprint('user', __name__)
user_service = UserService(UserRepositoryImpl())


@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_service.create_user(data['username'])
    return jsonify(id=user.id, username=user.username)


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(id=user.id, username=user.username)
    return jsonify(message='User not found'), 404
