from abc import ABC, abstractmethod
from app.applicant.domain.entities.applicant_documents import ApplicantDocuments
from typing import List

class ApplicantDocumentsRepository(ABC):

    @abstractmethod
    def get_by_id(self, document_id: int) -> ApplicantDocuments:
        pass

    @abstractmethod
    def add(self, applicant_document: ApplicantDocuments) -> ApplicantDocuments:
        pass

    @abstractmethod
    def get_all(self) -> List[ApplicantDocuments]:
        pass

    """@abstractmethod
    def update(self, applicant_document: ApplicantDocuments) -> ApplicantDocuments:
        pass

    @abstractmethod
    def delete(self, document_id: int) -> None:
        pass"""
