from flask import Blueprint, request, jsonify, current_app
from app.applicant.application.input.announcement_input_dto import AnnouncementInputDTO
from app.applicant.application.services.announcement_service import AnnouncementService
from app.applicant.infrastructure.repositories.announcement_repository_impl import AnnouncementRepositoryImpl
from app.applicant.domain.entities.announcement import Announcement

announcement_controller = Blueprint('announcement_controller', __name__)
announcement_service = AnnouncementService(AnnouncementRepositoryImpl())

@announcement_controller.route('', methods=['POST'])
def create_announcement():
    data = request.get_json()
    announcement_input = AnnouncementInputDTO(
        title=data["title"],
        description=data["description"],
        status=data["status"],
        location_id=data["location_id"],
        user_company_id=data["user_company_id"],
        publication_status=data["publication_status"]
    )
    announcement = announcement_service.create_announcement(announcement_input)
    return jsonify({
        "code": 200,
        "message": "Announcement created successfully",
        "data": announcement.to_dict()
    }), 200

@announcement_controller.route('/<int:announcement_id>', methods=['GET'])
def get_announcement(announcement_id):
    announcement = announcement_service.get_announcement(announcement_id)
    if announcement:
        return jsonify(announcement.to_dict()), 200
    return jsonify(message='Announcement not found'), 404

@announcement_controller.route('/', methods=['GET'])
def get_all_announcement():
    announcements = announcement_service.get_all_announcement()
    if announcements:
        announcements_list = [announcement.to_dict() for announcement in announcements]
        return jsonify(announcements_list), 200
    return jsonify(message='Announcements not found'), 404

@announcement_controller.route('/add', methods=['POST'])
def add_announcement():
    # Obtener los datos del anuncio desde el JSON del cuerpo de la solicitud
    data = request.get_json()

    announcement = Announcement(
        title=data.get('title'),
        description=data.get('description'),
        status=data.get('status'),
        location_id=data.get('location_id'),
        user_company_id=data.get('user_company_id'),
        publication_status=data.get('publication_status')
    )
    try:
        new_announcement = announcement_service.add(announcement)
        current_app.logger.info(f'Anuncio agregado: {new_announcement.to_dict()}')
        return jsonify(new_announcement.to_dict()), 201  # Devuelve el anuncio agregado y el código 201 (Created)
    except Exception as e:
        current_app.logger.error(f'Error al agregar el anuncio: {e}')
        return jsonify(message='Error al agregar el anuncio'), 500