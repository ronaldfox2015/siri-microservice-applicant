from app.applicant.domain.model.applicant_documents import ApplicantDocumentsModel
from app.applicant.domain.repositories.applicant_documents_repository import ApplicantDocumentsRepository
from app.applicant.domain.repositories.openai_repository import OpenaiRepository
from app.applicant.domain.entities.applicant_documents import ApplicantDocuments # Asegúrate de importar la entidad

class ApplicantDocumentsService:

    def __init__(self, applicant_documents_repository: ApplicantDocumentsRepository):
        self.applicant_documents_repository = applicant_documents_repository

    def create_applicant_document(self, applicant_document: ApplicantDocuments):
        return self.applicant_documents_repository.add(applicant_document)

    def get_all_applicant_documents(self):
        return self.applicant_documents_repository.get_all()
    
class ApplicantDocumentsApplyService:

    def __init__(self, openai_repository: OpenaiRepository):
        self.openai_repository = openai_repository

    def execute(self, prompt):
        result = self.openai_repository.search_by_prompt(prompt=prompt)
        return result
