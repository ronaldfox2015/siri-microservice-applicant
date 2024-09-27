from flask import Blueprint, request, jsonify

post_health = Blueprint('post', __name__)


@post_health.route('/health', methods=['GET'])
def verify_get():
    return jsonify(alive=True)
