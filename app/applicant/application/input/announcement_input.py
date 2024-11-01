class AnnouncementInput:
    def __init__(self, title, description, status, location_id, user_company_id, publication_status):
        self.title = title
        self.description = description
        self.status = status
        self.location_id = location_id
        self.user_company_id = user_company_id
        self.publication_status = publication_status

    def validate(self):
        if not isinstance(self.title, str) or len(self.title) > 255:
            raise ValueError("title must be a string with a maximum length of 255.")
        if not isinstance(self.description, str):
            raise ValueError("description must be a string.")
        if self.status not in ('active', 'inactive'):
            raise ValueError("status must be either 'active' or 'inactive'.")
        if not isinstance(self.location_id, int) or self.location_id <= 0:
            raise ValueError("location_id must be a positive integer.")
        if not isinstance(self.user_company_id, int) or self.user_company_id <= 0:
            raise ValueError("user_company_id must be a positive integer.")
        if self.publication_status not in ('published', 'draft'):
            raise ValueError("publication_status must be either 'published' or 'draft'.")
