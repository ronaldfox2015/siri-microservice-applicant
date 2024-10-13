from datetime import datetime


class User:
    def __init__(self, email="", password="", role="", activation_token=None, expiration_token=None, status=1, id=None):
        self.id = id
        self.email = email
        self.password = password
        self.role = role
        self.activation_token = activation_token
        self.expiration_token = expiration_token
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.status = status

    def __repr__(self):
        return f"<User {self.username}>"

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