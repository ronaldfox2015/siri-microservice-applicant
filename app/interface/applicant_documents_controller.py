from flask import Blueprint, request, jsonify, current_app
from app.applicant.application.input.announcement_input_dto import AnnouncementInputDTO
from app.applicant.application.services.applicant_documents_service import ApplicantDocumentsService
from app.applicant.infrastructure.repositories.applicant_documents_repository_impl import ApplicantDocumentsRepositoryImpl
from app.applicant.domain.entities.applicant_documents import ApplicantDocuments
from werkzeug.utils import secure_filename
import os

applicant_documents_controller = Blueprint('applicant_documents_controller', __name__)
applicant_documents_service = ApplicantDocumentsService(ApplicantDocumentsRepositoryImpl())

@applicant_documents_controller.route('/', methods=['GET'])
def get_all_applicant_documents():
    applicantDocuments = applicant_documents_service.get_all_applicant_documents()
    if applicantDocuments:
        applicant_documents_list = [applicantDocument.to_dict() for applicantDocument in applicantDocuments]
        return jsonify(applicant_documents_list), 200
    return jsonify(message='Applicant Documents not found'), 404

@applicant_documents_controller.route('/upload', methods=['POST'])
def upload_applicant_document():
    if 'file' not in request.files:
        return jsonify(message='No file part'), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(message='No selected file'), 400

    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        applicant_document = ApplicantDocuments(
            applicant_id=request.form.get('applicant_id'),
            file_name=filename,
            file_path=file_path,
            status=True
        )
        applicant_documents_service.create_applicant_document(applicant_document)

        return jsonify(message='File uploaded successfully'), 201
    return jsonify(message='File format not supported'), 400