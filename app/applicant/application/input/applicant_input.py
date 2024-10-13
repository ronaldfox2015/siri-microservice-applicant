class ApplicantInput:
    def __init__(self, user_id, first_name, last_name_father, last_name_mother, age, date_of_birth):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name_father = last_name_father
        self.last_name_mother = last_name_mother
        self.age = age
        self.date_of_birth = date_of_birth

    def validate(self):
        if not isinstance(self.user_id, int) or self.user_id <= 0:
            raise ValueError("user_id must be a positive integer.")
        if not isinstance(self.first_name, str) or len(self.first_name) > 100:
            raise ValueError("first_name must be a string with a maximum length of 100.")
        if not isinstance(self.last_name_father, str) or len(self.last_name_father) > 100:
            raise ValueError("last_name_father must be a string with a maximum length of 100.")
        if not isinstance(self.last_name_mother, str) or len(self.last_name_mother) > 100:
            raise ValueError("last_name_mother must be a string with a maximum length of 100.")
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("age must be a non-negative integer.")
        if not isinstance(self.date_of_birth, str):
            raise ValueError("date_of_birth must be a string representing a date in the format YYYY-MM-DD.")
