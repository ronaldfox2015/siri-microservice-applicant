import unittest
from unittest.mock import MagicMock

from app.applicant.domain.model.applicant import ApplicantModel
from app.applicant.domain.repositories.applicant_repository import ApplicantRepository


# Definimos un mock Applicant para usar en los tests
class MockApplicant:
    def __init__(self, user_id):
        self.user_id = user_id

    def to_dict(self):
        return {"user_id": self.user_id}


class TestApplicantModel(unittest.TestCase):

    def setUp(self):
        # Crear el mock del ApplicantRepository
        self.applicant_repository = MagicMock(spec=ApplicantRepository)
        # Crear la instancia de ApplicantModel con el repositorio simulado
        self.applicant_model = ApplicantModel(applicant_repository=self.applicant_repository)

    def test_add_new_applicant_successful(self):
        """Prueba correcta: Agregar un postulante nuevo exitosamente"""
        # Crear un postulante simulado
        mock_applicant = MockApplicant(user_id=1)

        # Simular que el postulante no existe en la base de datos
        self.applicant_repository.get_by_user_id.return_value = None

        # Simular que el método add regresa el postulante después de ser agregado
        self.applicant_repository.add.return_value = mock_applicant

        # Llamar al método add de ApplicantModel
        result = self.applicant_model.add(mock_applicant)

        # Asegurarse de que el resultado sea el diccionario del postulante
        self.assertEqual(result, {"user_id": 1})

        # Verificar que se llamaron a los métodos correctos
        self.applicant_repository.get_by_user_id.assert_called_once_with(mock_applicant.user_id)
        self.applicant_repository.add.assert_called_once_with(mock_applicant)

    def test_add_existing_applicant_raises_keyerror(self):
        """Prueba incorrecta: Lanzar KeyError si el postulante ya existe"""
        # Crear un postulante simulado
        mock_applicant = MockApplicant(user_id=1)

        # Simular que el postulante ya existe en la base de datos
        self.applicant_repository.get_by_user_id.return_value = mock_applicant

        # Verificar que el método add lance un KeyError
        with self.assertRaises(KeyError) as context:
            self.applicant_model.add(mock_applicant)
            print(context.exception)
            # Asegurarse de que el mensaje de error sea correcto
            self.assertEqual(str(context.exception), "El postulante ya existe.")

            # Verificar que se llamó a get_by_user_id con el user_id correcto
            self.applicant_repository.get_by_user_id.assert_called_once_with(mock_applicant.user_id)

            # Asegurarse de que `add` no fue llamado porque ya existe el postulante
            self.applicant_repository.add.assert_not_called()



