class UserInputDTO:
    def __init__(self, email: str, password: str, role: str):
        self.email = email
        self.password = password
        self.role = role

    def set_confirm_password(self, confirm_password):
        self.confirm_password = confirm_password

    def __repr__(self):
        return f"UserInputDTO(email={self.email}, password=***, role={self.role})"
