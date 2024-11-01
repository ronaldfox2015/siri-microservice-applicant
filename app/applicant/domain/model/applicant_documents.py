from app.applicant.domain.repositories.applicant_documents_repository import ApplicantDocumentsRepository
from app.applicant.domain.entities.applicant_documents import ApplicantDocuments

class ApplicantDocumentsModel:
    def __init__(self, applicant_documents_repository: ApplicantDocumentsRepository) -> None:
        self.applicant_documents_repository = applicant_documents_repository

    def add(self, applicant_document: ApplicantDocuments):
        existing_document = self.applicant_documents_repository.get_by_id(applicant_document.id)
        if existing_document is not None:
            raise KeyError("El documento del solicitante ya existe.")

        model = self.applicant_documents_repository.add(applicant_document)
        return model.to_dict()
