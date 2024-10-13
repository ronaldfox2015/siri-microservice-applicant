
from app.applicant.domain.entities.user import User
from app.applicant.domain.repositories.user_repository import UserRepository
from app.applicant.infrastructure.db.models import db, UserModelOrm
from sqlalchemy import and_


class UserRepositoryImpl(UserRepository):
    def get_by_id(self, user_id: int) -> User:
        user_model = UserModelOrm.query.get(user_id)
        if user_model:
            return None
        return None

    def add(self, user) -> User:
        new_user = UserModelOrm(**vars(user))
        db.session.add(new_user)
        db.session.commit()
        new_user.id = new_user.id
        return User(
                id=new_user.id,
                email=new_user.email,
                password=new_user.password,
                role=new_user.role,
                activation_token=new_user.activation_token,
                expiration_token=new_user.expiration_token,
                status=new_user.status
            )

    def get_by_mail(self, email: str, role: str) -> User:
        user_model = UserModelOrm.query.filter(
            and_(UserModelOrm.email == email, UserModelOrm.role == role)
        ).first()
        if user_model:
            return User(
                id=user_model.id,
                email=user_model.email,
                password=user_model.password,
                role=user_model.role,
                activation_token=user_model.activation_token,
                expiration_token=user_model.expiration_token,
                status=user_model.status
            )
        return None

    def all_by_mail(self, email: str, role: str) -> [User]:
        return UserModelOrm.query.filter(
            and_(UserModelOrm.email == email, UserModelOrm.role == role)
        ).all()
