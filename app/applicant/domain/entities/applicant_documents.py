class ApplicantDocuments:
    def __init__(self, id: int = None, applicant_id: int = None, file_name: str = None,
                 file_path: str = None, created_at: str = None, updated_at: str = None, 
                 status: bool = False):
        self.id = id  # Se asignará más tarde cuando se inserte en la base de datos
        self.applicant_id = applicant_id
        self.file_name = file_name
        self.file_path = file_path
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "applicant_id": self.applicant_id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status
        }
