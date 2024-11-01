from app.applicant.domain.repositories.announcement_repository import AnnouncementRepository
from app.applicant.domain.entities.announcement import Announcement

class AnnouncementModel:
    def __init__(self, announcement_repository: AnnouncementRepository) -> None:
        self.announcement_repository = announcement_repository

    def add(self, announcement: Announcement):
        existing_announcement = self.announcement_repository.get_by_id(announcement.id)
        if existing_announcement is not None:
            raise KeyError("El anuncio ya existe.")

        model = self.announcement_repository.add(announcement)
        return model.to_dict()
