from flask import Blueprint, current_app, request, jsonify

from applicant.application.input.applicant_input import ApplicantInput
from applicant.application.services.applicant_service import ApplicantService
from applicant.infrastructure.repositories.applicant_repository_impl import ApplicantRepositoryImpl

from applicant.application.services.applicant_service import ApplyService
from applicant.infrastructure.repositories.openai_repository_impl import OpenaiRepositoryImpl

applicant_controller = Blueprint('applicant', __name__)
applicant_service = ApplicantService(ApplicantRepositoryImpl())
apply_service = ApplyService(OpenaiRepositoryImpl())


@applicant_controller.route('', methods=['POST'])
def create_applicant():
    data = request.get_json()
    applicant_input = ApplicantInput(
        user_id=data["user_id"],
        first_name=data["first_name"],
        last_name_father=data["last_name_father"],
        last_name_mother=data["last_name_mother"],
        age=data["age"],
        date_of_birth=data["date_of_birth"]
    )
    applicant_input.validate()

    return jsonify({
        "code": 200*100,
        "message": "ok",
        "data": applicant_service.create_applicant(applicant_input)
    }), 200

