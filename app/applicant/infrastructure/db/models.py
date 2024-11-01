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