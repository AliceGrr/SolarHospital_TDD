from unittest.mock import MagicMock

from patients_repository import PatientsRepository


def test_get_status():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    user_dialog = MagicMock()
    hospital_handler = HospitalHandler(patients_repository, user_dialog)

    hospital_handler.get_status(1)

    user_dialog.print_status.assert_called_with('Слегка болен')
