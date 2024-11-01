from applicant.domain.repositories.applicant_repository import ApplicantRepository


class ApplicantModel:
    password: str

    def __init__(self, applicant_repository: ApplicantRepository) -> None:
        self.applicant_repository = applicant_repository

    def add(self, applicant):
        applicant_repository = self.applicant_repository.get_by_user_id(applicant.user_id)
        if applicant_repository is not None:
            raise KeyError("El postulante ya existe.")

        model = self.applicant_repository.add(applicant)
        return model.to_dict()