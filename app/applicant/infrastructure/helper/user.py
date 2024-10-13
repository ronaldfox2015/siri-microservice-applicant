import jwt
import datetime

# Clave secreta para firmar el token (¡mantén esto seguro!)
SECRET_KEY = 'siri2024'


# Crear un token con datos de usuario y fecha de expiración
def generate_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiración en 1 hora
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return "El token ha expirado"
    except jwt.InvalidTokenError:
        return "Token inválido"
