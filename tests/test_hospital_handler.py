from unittest.mock import MagicMock

from hospital_handler import HospitalHandler
from patients_repository import PatientsRepository


def test_get_status():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    user_dialog = MagicMock()
    user_dialog.input_patient_id = MagicMock(return_value=1)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.get_status()

    user_dialog.print_status.assert_called_with('Слегка болен')


def test_status_down():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    user_dialog = MagicMock()
    user_dialog.input_patient_id = MagicMock(return_value=1)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.status_down()

    user_dialog.print_status_changed.assert_called_with('Болен')
    assert patients_repository._patients_base == [2, 2, 1, 0]
