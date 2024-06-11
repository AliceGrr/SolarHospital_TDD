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


def test_get_status_when_patient_not_exists():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['показать статус', '99', 'стоп']

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
            call('Такого пациента нет в больнице'),
            call('Работа закончена')
        ],
        any_order=False
    )


def test_get_status_when_string_patient_id():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['показать статус', 'два', 'стоп']

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
            call('ID пациента должно быть положительным числом'),
            call('Работа закончена')
        ],
        any_order=False
    )


def test_status_down():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['понизить статус', '1', 'стоп']

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
            call('Новый статус пациента: "Болен"'),
            call('Работа закончена')
        ],
        any_order=False
    )
    assert patients_repository._patients_base == [1, 3, 1, 0]


def test_status_down_when_patient_stats_minimum():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['понизить статус', '4', 'стоп']

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
            call('Статус нельзя понизить (никто не умирает у нас)'),
            call('Работа закончена')
        ],
        any_order=False
    )
    assert patients_repository._patients_base == [2, 3, 1, 0]


def test_discharge():
    patients_repository = PatientsRepository([2, 3, 1, 0])
    console_mock = MagicMock()
    user_dialog = UserDialog(console_mock)
    hospital_handler = HospitalHandler(user_dialog, patients_repository)
    hospital = Hospital(hospital_handler, user_dialog)

    console_mock.input.side_effect = ['выписать', '1', 'стоп']

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
            call('Пациент выписан'),
            call('Работа закончена')
        ],
        any_order=False
    )
    assert patients_repository._patients_base == [3, 1, 0]