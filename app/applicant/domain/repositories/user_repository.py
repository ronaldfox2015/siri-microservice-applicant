from abc import ABC, abstractmethod
from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def add(self, user: User) -> None:
        pass
