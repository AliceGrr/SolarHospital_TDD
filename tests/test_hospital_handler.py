from unittest.mock import MagicMock

from hospital_handler import HospitalHandler
from patients_repository import PatientsRepository
from user_dialog import UserDialog


def test_get_status():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 1
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.get_status()

    console_mock.assert_called_with('Статус пациента: "Слегка болен"')


def test_status_down():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    user_dialog = MagicMock()
    user_dialog.input_patient_id = MagicMock(return_value=1)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.status_down()

    user_dialog.print_status_changed.assert_called_with('Болен')
    assert patients_repository._patients_base == [1, 3, 1, 0]


def test_discharge():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    user_dialog = MagicMock()
    user_dialog.input_patient_id = MagicMock(return_value=1)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.discharge()

    user_dialog.print_patient_discharged.assert_called()
    assert patients_repository._patients_base == [3, 1, 0]

