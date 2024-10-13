from app.notification.application.send_input_dto import SendInputDTO
from app.notification.domain.items import ItemsEntity, Addressee, MailBody
from app.notification.domain.mail_repository import MailRepository


class MailService:
    def __init__(self, mail_repository: MailRepository):
        self.mail_repository = mail_repository

    def execute(self, sendInputDTO: SendInputDTO):
        itemsEntity = ItemsEntity()
        addressee = Addressee()
        addressee.To = sendInputDTO.To
        addressee.From = sendInputDTO.From
        addressee.Subject = sendInputDTO.Subject
        itemsEntity.addressee = addressee

        mailBody = MailBody()
        mailBody.slug = sendInputDTO.template
        mailBody.recipient_data = sendInputDTO.recipient_data
        mailBody.html = self.mail_repository.html(mailBody)

        itemsEntity.mailBody = mailBody
        self.mail_repository.send(itemsEntity)