from app.applicant.domain.entities.applicant_documents import ApplicantDocuments
from app.applicant.domain.repositories.applicant_documents_repository import ApplicantDocumentsRepository
from app.applicant.infrastructure.db.models import ApplicantDocumentsModelOrm, db
from typing import List
from flask import current_app
from sqlalchemy import and_

class ApplicantDocumentsRepositoryImpl(ApplicantDocumentsRepository):
    
    def get_all(self) -> List[ApplicantDocuments]:
        document_models = ApplicantDocumentsModelOrm.query.all()
        return [
            ApplicantDocuments(
                id=document_model.id,
                applicant_id=document_model.applicant_id,
                file_name=document_model.file_name,
                file_path=document_model.file_path,
                created_at=document_model.created_at,
                updated_at=document_model.updated_at,
                status=document_model.status
            )
            for document_model in document_models
        ]

    def get_by_id(self, document_id: int) -> ApplicantDocuments:
        document_model = ApplicantDocumentsModelOrm.query.filter(
            and_(ApplicantDocumentsModelOrm.id == document_id)
        ).first()
        current_app.logger.info(f'ApplicantDocumentsRepositoryImpl: Retrieved document {document_model}')
        if document_model:
            return ApplicantDocuments(
                id=document_model.id,
                applicant_id=document_model.applicant_id,
                file_name=document_model.file_name,
                file_path=document_model.file_path,
                created_at=document_model.created_at,
                updated_at=document_model.updated_at,
                status=document_model.status
            )
        return None

    def add(self, applicant_document: ApplicantDocuments) -> ApplicantDocuments:
        new_document = ApplicantDocumentsModelOrm(**vars(applicant_document))
        db.session.add(new_document)
        db.session.commit()
        current_app.logger.info(f'ApplicantDocumentsRepositoryImpl: Added document {new_document.to_dict()}')
        
        return ApplicantDocuments(
            id=new_document.id,
            applicant_id=new_document.applicant_id,
            file_name=new_document.file_name,
            file_path=new_document.file_path,
            created_at=new_document.created_at,
            updated_at=new_document.updated_at,
            status=new_document.status
        )
