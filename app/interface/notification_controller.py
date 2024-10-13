from flask import Blueprint, current_app, request, jsonify

from app.notification.application.mai_service import MailService
from app.notification.application.send_input_dto import SendInputDTO
from app.notification.infrastructure.mail_repository_imp import MailRepositoryImpl
import os

notification_controller = Blueprint('notification', __name__)
notification_service = MailService(MailRepositoryImpl(
    {
        "smtp_server": os.getenv("MAIL_HOST"),
        "smtp_port": os.getenv("MAIL_PORT"),
        "username": os.getenv("MAIL_USER"),
        "password": os.getenv("MAIL_PASSWORD")
    }
))


@notification_controller.route('', methods=['POST'])
def send():
    data = request.get_json()
    user_input = SendInputDTO(
        From=data["from"],
        To=data["to"],
        Subject=data["subject"],
        template=data["template"],
        recipient_data=data["data"]
    )

    return jsonify({
        "code": 200*100,
        "message": "ok",
        "data": notification_service.execute(user_input)
    }), 200