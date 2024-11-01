import bcrypt

from applicant.application.input.user_input_dto import UserInputDTO
from applicant.domain.entities.user import User
from applicant.domain.repositories.user_repository import UserRepository
from flask import current_app


class UserModel:
    password: str

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def add(self, user: UserInputDTO):
        user.password = self.hash_password(user.password)
        del user.confirm_password
        return self.user_repository.add(user)

    def email_and_password(self, user: UserInputDTO) -> User:
        user_repository = self.user_repository.get_by_mail(email=user.email,role=user.role)
        if self.check_password(user.password, user_repository.password):
            return user_repository
        return User()

    def validate_register(self, user: UserInputDTO):
        user_repository = self.user_repository.all_by_mail(email=user.email, role=user.role)
        current_app.logger.info(f'UserModel recibidos: {user_repository}')
        if len(user_repository) > 0:
            raise KeyError("El usuario ya existe.")

        if user.password != user.confirm_password:
            raise KeyError("El password y confirm_password son diferentes.")

        return True

    def validate_login(self, user: UserInputDTO):
        user_repository = self.user_repository.all_by_mail(email=user.email, role=user.role)
        if len(user_repository) == 0:
            raise KeyError("El usuario no esta registrado.")

        if user_repository is not None:
            if user.password != user.confirm_password:
                raise KeyError("El password y confirm_password son diferentes.")

            if len(user_repository) > 1:
                raise KeyError("Existe un usuario con esta cuenta contactar con soporte@gmail.com.")

            if not self.check_password(user.password, user_repository[0].password):
                raise KeyError("El usuario ya existe.")

        return True

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
