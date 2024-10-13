from app.applicant.application.input.user_input_dto import UserInputDTO
from app.applicant.domain.entities.user import User
from app.applicant.domain.model.user import UserModel
from app.applicant.domain.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, param: UserInputDTO):
        model = UserModel(self.user_repository)
        user = User()
        if model.validate_register(param):
            user = model.add(param)
        return user.to_dict()

    def auth_login(self, param):
        model = UserModel(self.user_repository)
        user = User()
        if model.validate_login(param):
            user = model.email_and_password(param)
        return user.to_dict()
