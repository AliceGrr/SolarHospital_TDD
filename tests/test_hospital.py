from unittest.mock import MagicMock, call

from hospital import Hospital
from hospital_handler import HospitalHandler
from patients_repository import PatientsRepository
from user_dialog import UserDialog


def test_get_status():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['показать статус', '1', 'стоп']

    hospital.start_work()

    console_mock.input.assert_has_calls(
        [
            call("Введите команду: "),
            call("Введите id пациента: "),
            call("Введите команду: "),
        ],
        any_order=False,
    )
    console_mock.print.assert_has_calls(
        [
            call('Статус пациента: "Слегка болен"'),
            call('Работа закончена')
        ],
        any_order=False
    )
