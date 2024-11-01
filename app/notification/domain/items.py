from abc import ABC


class Addressee:
    From: str
    To: str
    Subject: str


class MailBody:
    slug: str
    html: str
    recipient_data: object


class ItemsEntity:
    addressee: Addressee
    mailBody: MailBody
