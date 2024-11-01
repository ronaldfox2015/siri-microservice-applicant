from abc import ABC, abstractmethod
from app.applicant.domain.entities.applicant import Applicant


class ApplicantRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Applicant:
        pass

    @abstractmethod
    def add(self, applicant) -> Applicant:
        pass
