from app.applicant.domain.model.applicant import ApplicantModel
from app.applicant.domain.repositories.applicant_repository import ApplicantRepository

from app.applicant.domain.repositories.openai_repository import OpenaiRepository


class ApplicantService:

    def __init__(self, applicant_repository: ApplicantRepository):
        self.applicant_repository = applicant_repository

    def create_applicant(self, param):
        model = ApplicantModel(self.applicant_repository)
        return model.add(applicant=param)


class ApplyService:

    def __init__(self, openai_repository: OpenaiRepository):
        self.openai_repository = openai_repository

    def execute(self, prompt):
        openai_repository = self.openai_repository.search_by_prompt(prompt=prompt)
        return openai_repository
