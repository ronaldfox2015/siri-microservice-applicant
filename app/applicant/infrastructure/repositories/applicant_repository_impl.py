from applicant.domain.entities.applicant import Applicant
from applicant.domain.repositories.applicant_repository import ApplicantRepository
from applicant.infrastructure.db.models import ApplicantModelOrm, db
from flask import current_app
from sqlalchemy import and_


class ApplicantRepositoryImpl(ApplicantRepository):
    def get_by_user_id(self, user_id: int) -> Applicant:
        applicant_model = ApplicantModelOrm.query.filter(
            and_(ApplicantModelOrm.user_id == user_id)
        ).first()
        current_app.logger.info(f'UserRepositoryImpl recibidos: {applicant_model}')
        if applicant_model:
            return applicant_model
        return None

    def add(self, applicant: Applicant) -> Applicant:
        new_applicant = ApplicantModelOrm(**vars(applicant))
        db.session.add(new_applicant)
        db.session.commit()
        current_app.logger.info(f'UserRepositoryImpl recibidos: {new_applicant.to_dict()}')
        applicant = Applicant(
            id=new_applicant.id,
            user_id=new_applicant.user_id,
            first_name=new_applicant.first_name,
            last_name_father=new_applicant.last_name_father,
            last_name_mother=new_applicant.last_name_mother,
            age=new_applicant.age,
            date_of_birth=new_applicant.date_of_birth,
            status=new_applicant.status
        )
        return applicant

