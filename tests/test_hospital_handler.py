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

    console_mock.print.assert_called_with('Статус пациента: "Слегка болен"')


def test_get_status_when_patient_not_exists():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 99
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.get_status()

    console_mock.print.assert_called_with('Такого пациента нет в больнице')


def test_get_status_when_invalid_patient_id():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = "два"
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.get_status()

    console_mock.print.assert_called_with('ID пациента должно быть положительным числом')


def test_status_down():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 1
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.status_down()

    console_mock.print.assert_called_with('Новый статус пациента: "Болен"')
    assert patients_repository._patients_base == [1, 3, 1, 0]


def test_status_down_when_patient_not_exists():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 99
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.status_down()

    console_mock.print.assert_called_with('Такого пациента нет в больнице')


def test_discharge():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 1
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.discharge()

    console_mock.print.assert_called_with('Пациент выписан')
    assert patients_repository._patients_base == [3, 1, 0]


def test_discharge_when_patient_not_exists():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    console_mock.input.return_value = 99
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)

    hospital_handler.discharge()

    console_mock.print.assert_called_with('Такого пациента нет в больнице')

