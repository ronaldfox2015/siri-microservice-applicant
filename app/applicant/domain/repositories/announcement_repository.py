from abc import ABC, abstractmethod
from app.applicant.domain.entities.announcement import Announcement
from typing import List

class AnnouncementRepository(ABC):
    @abstractmethod
    def get_by_id(self, announcement_id: int) -> Announcement:
        pass

    @abstractmethod
    def add(self, announcement: Announcement) -> Announcement:
        pass

    @abstractmethod
    def get_all(self) -> List[Announcement]:
        pass

    """@abstractmethod
    def update(self, announcement: Announcement) -> Announcement:
        pass

    @abstractmethod
    def delete(self, announcement_id: int) -> None:
        pass"""
