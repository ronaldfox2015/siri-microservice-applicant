from app.applicant.domain.model.announcement import AnnouncementModel
from app.applicant.domain.repositories.announcement_repository import AnnouncementRepository
from app.applicant.domain.repositories.openai_repository import OpenaiRepository


class AnnouncementService:

    def __init__(self, announcement_repository: AnnouncementRepository):
        self.announcement_repository = announcement_repository

    def create_announcement(self, param):
        model = AnnouncementModel(self.announcement_repository)
        return model.add(announcement=param)

    def get_announcement(self, announcement_id):
        return self.announcement_repository.get_by_id(announcement_id)
    
    def get_all_announcement(self):
        return self.announcement_repository.get_all()
    
class AnnouncementApplyService:

    def __init__(self, openai_repository: OpenaiRepository):
        self.openai_repository = openai_repository

    def execute(self, prompt):
        result = self.openai_repository.search_by_prompt(prompt=prompt)
        return result
