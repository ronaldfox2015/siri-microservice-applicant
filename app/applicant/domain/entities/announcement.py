class Announcement:
    def __init__(self, id: int = None, title: str = None, description: str = None, 
                 status: str = 'inactive', location_id: int = None, 
                 user_company_id: int = None, publication_status: str = 'draft'):
        self.id = id  # Se asignará más tarde cuando se inserte en la base de datos
        self.title = title
        self.description = description
        self.status = status
        self.location_id = location_id
        self.user_company_id = user_company_id
        self.publication_status = publication_status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "location_id": self.location_id,
            "user_company_id": self.user_company_id,
            "publication_status": self.publication_status
        }
