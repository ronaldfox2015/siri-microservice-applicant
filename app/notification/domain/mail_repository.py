from abc import ABC, abstractmethod

from notification.domain.items import ItemsEntity, MailBody


class MailRepository(ABC):

    @abstractmethod
    def send(self, itemsEntity: ItemsEntity):
        pass

    @abstractmethod
    def html(self, itemsEntity: MailBody):
        pass