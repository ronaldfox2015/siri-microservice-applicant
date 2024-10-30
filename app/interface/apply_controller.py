from flask import Blueprint, current_app, request, jsonify

from applicant.application.services.applicant_service import ApplicantService, ApplyService
from applicant.infrastructure.repositories.applicant_repository_impl import ApplicantRepositoryImpl
from applicant.infrastructure.repositories.openai_repository_impl import OpenaiRepositoryImpl

apply_controller = Blueprint('apply', __name__)
applicant_service = ApplicantService(ApplicantRepositoryImpl())
apply_service = ApplyService(OpenaiRepositoryImpl())


@apply_controller.route('<int:id>/apply', methods=['POST'])
def apply(id):
    return jsonify({
        "code": 200*100,
        "message": "ok",
        "data": apply_service.execute('')
    }), 200