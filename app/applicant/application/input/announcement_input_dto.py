class AnnouncementInputDTO:
    def __init__(self, title: str, description: str, status: str, location_id: int, user_company_id: int, publication_status: str):
        self.title = title
        self.description = description
        self.status = status
        self.location_id = location_id
        self.user_company_id = user_company_id
        self.publication_status = publication_status

    def __repr__(self):
        return (f"AnnouncementInputDTO(title={self.title}, description=***, status={self.status}, "
                f"location_id={self.location_id}, user_company_id={self.user_company_id}, "
                f"publication_status={self.publication_status})")
