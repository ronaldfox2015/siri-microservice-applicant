class SendInputDTO:
    def __init__(self, From: str, To: str, Subject: str, template: str, recipient_data: str):
        self.template = template
        self.From = From
        self.To = To
        self.Subject = Subject
        self.recipient_data = recipient_data

