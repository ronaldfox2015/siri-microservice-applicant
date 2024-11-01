from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModelOrm(db.Model):
    __tablename__ = 'user'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='Unique identifier')
    email = db.Column(db.String(255), nullable=False, comment='User email address')
    password = db.Column(db.String(255), nullable=False, comment='User password (hashed)')
    role = db.Column(db.Enum('postulante', 'empresa-usuario', 'empresa-admin'), nullable=False, comment='User role')
    activation_token = db.Column(db.String(255), nullable=True, comment='Activation token')
    expiration_token = db.Column(db.DateTime, nullable=True, comment='Activation token expiration date')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, comment='Creation date')
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment='Last update date')
    status = db.Column(db.Boolean, nullable=False, default=True, comment='Account status (active/inactive)')

    user_company = db.relationship('UserCompanyModelOrm', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"

    def to_dict(self):
        """Convierte la instancia a un diccionario."""
        return {
            'id': self.id,
            'email': self.email,
            'role': self.role,
            'activation_token': self.activation_token,
            'expiration_token': self.expiration_token,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'status': self.status
        }


class ApplicantModelOrm(db.Model):
    __tablename__ = 'applicant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name_father = db.Column(db.String(100), nullable=False)
    last_name_mother = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Integer, default=1)

    applicant_documents = db.relationship("ApplicantDocumentsModelOrm", back_populates="applicant")

    def __repr__(self):
        return (f"<Applicant(id={self.id}, user_id={self.user_id}, first_name='{self.first_name}', "
                f"last_name_father='{self.last_name_father}', last_name_mother='{self.last_name_mother}', "
                f"age={self.age}, date_of_birth={self.date_of_birth}, status={self.status})>")

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

class AnnouncementModelOrm(db.Model):
    __tablename__ = 'announcement'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum('active', 'inactive'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    user_company_id = db.Column(db.Integer, db.ForeignKey('user_company.id'), nullable=False)
    publication_status = db.Column(db.Enum('published', 'draft'), nullable=False)
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    location = db.relationship('LocationModelOrm', back_populates='announcements')
    user_company = db.relationship('UserCompanyModelOrm', back_populates='announcements')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "location_id": self.location_id,
            "user_company_id": self.user_company_id,
            "publication_status": self.publication_status
            #"created_at": self.created_at,
            #"updated_at": self.updated_at
        }


class LocationModelOrm(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    code = db.Column(db.String(2), nullable=True)
    display_name = db.Column(db.String(200), nullable=True)
    search_name = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(200), nullable=True)
    capital_id = db.Column(db.Integer, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    children_count = db.Column(db.Integer, nullable=True)
    level = db.Column(db.SmallInteger, nullable=True)
    adecsys_id = db.Column(db.Integer, nullable=True)
    ad_count = db.Column(db.Integer, nullable=True)
    index_name = db.Column(db.String(200), nullable=True)
    country_code = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    department_code = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=True)
    province_code = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=True)
    district_code = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=True)
    status = db.Column(db.Boolean, nullable=False, default=True)

    # Relaciones con tablas de clave foránea
    #country = db.relationship('Country', backref=db.backref('locations', lazy=True))
    #department = db.relationship('Department', backref=db.backref('locations', lazy=True))
    #province = db.relationship('Province', backref=db.backref('locations', lazy=True))
    #district = db.relationship('District', backref=db.backref('locations', lazy=True))
    #parent_location = db.relationship('Location', remote_side=[id], backref=db.backref('sub_locations', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "parent_id": self.parent_id,
            "code": self.code,
            "display_name": self.display_name,
            "search_name": self.search_name,
            "slug": self.slug,
            "capital_id": self.capital_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "children_count": self.children_count,
            "level": self.level,
            "adecsys_id": self.adecsys_id,
            "ad_count": self.ad_count,
            "index_name": self.index_name,
            "country_code": self.country_code,
            "department_code": self.department_code,
            "province_code": self.province_code,
            "district_code": self.district_code,
            "status": self.status
        }

    announcements = db.relationship('AnnouncementModelOrm', back_populates='location')

class UserCompanyModelOrm(db.Model):
    __tablename__ = 'user_company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    role = db.Column(db.Enum('admin', 'employee', 'manager'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)

    user = db.relationship('UserModelOrm', back_populates='user_company')
    #company = db.relationship('Company', backref=db.backref('user_companies', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_id": self.company_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "role": self.role,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "status": self.status
        }

    announcements = db.relationship('AnnouncementModelOrm', back_populates='user_company')

class ApplicantDocumentsModelOrm(db.Model):
    __tablename__ = 'applicant_documents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.Boolean, nullable=False)

    applicant = db.relationship('ApplicantModelOrm', back_populates='applicant_documents')

    def __repr__(self):
        return f"<ApplicantDocuments(id={self.id}, applicant_id={self.applicant_id}, file_name='{self.file_name}')>"

    def to_dict(self):
        return {
            "id": self.id,
            "applicant_id": self.applicant_id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "status": self.status
        }

    
    