from abc import ABC, abstractmethod

from applicant.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def add(self, user) -> None:
        pass

    @abstractmethod
    def get_by_mail(self, email: str, role: str) -> User:
        pass

    @abstractmethod
    def all_by_mail(self, email: str, role: str) -> [User]:
        pass