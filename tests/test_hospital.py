from unittest.mock import MagicMock

from hospital_handler import HospitalHandler
from patients_repository import PatientsRepository
from user_dialog import UserDialog


def test_get_status():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    hospital.start_work()

    console_mock.input.return_value = ['get status', '1', 'stop']

    console_mock.input.assert_called_with([
        "Введите команду: ",
        "Введите id пациента: ",
        "Введите команду: ",
    ])
    console_mock.print.assert_called_with([
        'Статус пациента: "Слегка болен"',
        'Работа закончена'
    ])