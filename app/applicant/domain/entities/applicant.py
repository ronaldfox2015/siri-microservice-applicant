class Applicant:
    def __init__(self, id: int, user_id: int, first_name: str, last_name_father: str, last_name_mother:str, age: int, date_of_birth, status: int):
        self.id = None  # Se asignará más tarde cuando se inserte en la base de datos
        self.user_id = user_id
        self.first_name = first_name
        self.last_name_father = last_name_father
        self.last_name_mother = last_name_mother
        self.age = age
        self.date_of_birth = date_of_birth
        self.created_at = None  # Se asignará en el momento de la creación
        self.updated_at = None  # Se asignará en el momento de la creación
        self.status = status


    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name_father": self.last_name_father,
            "last_name_mother": self.last_name_mother,
            "age": self.age,
            "date_of_birth": self.date_of_birth,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status
        }