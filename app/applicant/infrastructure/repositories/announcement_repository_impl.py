from app.applicant.domain.entities.announcement import Announcement
from app.applicant.domain.repositories.announcement_repository import AnnouncementRepository
from app.applicant.infrastructure.db.models import AnnouncementModelOrm, db
from typing import List
from flask import current_app
from sqlalchemy import and_

class AnnouncementRepositoryImpl(AnnouncementRepository):
    def get_by_id(self, announcement_id: int) -> Announcement:
        announcement_model = AnnouncementModelOrm.query.filter(
            and_(AnnouncementModelOrm.id == announcement_id)
        ).first()
        current_app.logger.info(f'AnnouncementRepositoryImpl recibidos: {announcement_model}')
        if announcement_model:
            return announcement_model
        return None

    def add(self, announcement: Announcement) -> Announcement:
        new_announcement = AnnouncementModelOrm(**vars(announcement))
        db.session.add(new_announcement)
        db.session.commit()
        current_app.logger.info(f'AnnouncementRepositoryImpl recibidos: {new_announcement.to_dict()}')
        
        # Crea un objeto Announcement a partir del nuevo anuncio en la base de datos
        announcement = Announcement(
            id=new_announcement.id,
            title=new_announcement.title,
            description=new_announcement.description,
            status=new_announcement.status,
            location_id=new_announcement.location_id,
            user_company_id=new_announcement.user_company_id,
            publication_status=new_announcement.publication_status
            #created_at=new_announcement.created_at,
            #updated_at=new_announcement.updated_at
        )
        return announcement
    
    def get_all(self) -> List[Announcement]:
        announcement_models = AnnouncementModelOrm.query.all()
        return [
            Announcement(
                id=announcement_model.id,
                title=announcement_model.title,
                description=announcement_model.description,
                status=announcement_model.status,
                location_id=announcement_model.location_id,
                user_company_id=announcement_model.user_company_id,
                publication_status=announcement_model.publication_status
                #created_at=announcement_model.created_at,
                #updated_at=announcement_model.updated_at
            )
            for announcement_model in announcement_models
        ]
