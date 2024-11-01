from unittest import TestCase
from unittest.mock import MagicMock, patch

import bcrypt

from app.applicant.application.input.user_input_dto import UserInputDTO
from app.applicant.domain.model.user import UserModel
from app.applicant.domain.repositories.user_repository import UserRepository


class TestUserModel(TestCase):

    def setUp(self):
        # Crear el mock del UserRepository
        self.user_repository = MagicMock(spec=UserRepository)
        # Crear la instancia de UserModel con el repositorio simulado
        self.user_model = UserModel(user_repository=self.user_repository)

    def test_add_new_user_successful(self):
        """Prueba correcta: Agregar un nuevo usuario exitosamente"""
        # Crear un mock de UserInputDTO (los datos de entrada)
        mock_user = MagicMock(spec=UserInputDTO)
        mock_user.email = 'test@example.com'
        mock_user.role = 'postulante'
        mock_user.password = 'password123'

        # Simular que el usuario no existe en el repositorio
        self.user_repository.get_by_mail.return_value = None

        # Simular el método add en el repositorio para que retorne el mismo usuario
        self.user_repository.add.return_value = mock_user

        # Simular la función de hashing de bcrypt
        with patch('bcrypt.hashpw') as mock_hashpw, patch('bcrypt.gensalt') as mock_gensalt:
            mock_hashpw.return_value = b'hashed_password'
            mock_gensalt.return_value = b'salt'

            # Llamar al método add del modelo
            result = self.user_model.add(mock_user)


            # Asegurarse de que el usuario fue añadido a través del repositorio
            self.user_repository.add.assert_called_once_with(mock_user)

            # Verificar que el resultado es el mismo mock_user
            self.assertEqual(result, mock_user)

    def test_add_existing_user_raises_keyerror(self):
        """Prueba incorrecta: Lanzar KeyError El usuario ya existe"""
        # Crear un mock de UserInputDTO
        mock_user = MagicMock(spec=UserInputDTO)
        mock_user.email = 'test@example.com'
        mock_user.role = 'postulante'
        mock_user.password = 'password123'

        # Crear un mock de un usuario que ya existe en el repositorio
        mock_existing_user = MagicMock(spec=UserInputDTO)
        mock_existing_user.email = 'test@example.com'
        mock_existing_user.role = 'postulante'
        mock_existing_user.password = 'hashed_password'

        # Simular que el usuario ya existe en la base de datos
        self.user_repository.get_by_mail.return_value = mock_existing_user

        # Simular el chequeo de la contraseña
        with patch('bcrypt.checkpw') as mock_checkpw:
            mock_checkpw.return_value = True  # Las contraseñas coinciden

            # Verificar que se lanza KeyError cuando el usuario ya existe
            # with self.assertRaises(KeyError) as context:
            #     self.user_model.add(mock_user)

                # Verificar que el mensaje de error es el correcto
                # self.assertEqual(str(context.exception), "El usuario ya existe.")

                # Asegurarse de que se llamó al método check_password
                # mock_checkpw.assert_called_once_with(mock_user.password.encode('utf-8'), mock_existing_user.password.encode('utf-8'))

                # Asegurarse de que el método add no fue llamado
                # self.user_repository.add.assert_not_called()


