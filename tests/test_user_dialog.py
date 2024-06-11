import unittest.mock

import pytest

from console_user_interface import ConsoleUserInterface
from constants import CommandTypes
from exceptions import InvalidPatientIdException
from user_dialog import UserDialog


@unittest.mock.patch('builtins.input', side_effect=['показать статус'])
def test_input_command_get_status(_):
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog.input_command()

    assert command == CommandTypes.GET_STATUS


@unittest.mock.patch('builtins.input', side_effect=['1'])
def test_input_id(_):
    dialog = UserDialog(ConsoleUserInterface())

    patient_id = dialog.input_patient_id()

    assert patient_id == 1


def test_convert_command_get_status():
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog._convert_command('показать статус')

    assert command == CommandTypes.GET_STATUS


def test_convert_command_when_unknown_user_command():
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog._convert_command('покажи все статусы')

    assert command == CommandTypes.UNKNOWN


test_data = [
    ('показать статус', CommandTypes.GET_STATUS),
    ('поКАЗАТЬ статус', CommandTypes.GET_STATUS),

    ('выписать', CommandTypes.DISCHARGE),
    ('понизить статус', CommandTypes.STATUS_DOWN),
    ('стоп', CommandTypes.STOP)
]


@pytest.mark.parametrize("user_input,command_type", test_data)
def test_user_input_and_command_mapping(user_input, command_type):
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog._convert_command(user_input)

    assert command == command_type


def test_convert_patient_id():
    dialog = UserDialog(ConsoleUserInterface())

    patient_id = dialog._convert_patient_id('1')

    assert patient_id == 1


def test_convert_patient_id_when_negative_id():
    dialog = UserDialog(ConsoleUserInterface())

    with pytest.raises(InvalidPatientIdException):
        _ = dialog._convert_patient_id('-1')


def test_convert_patient_id_when_string_id():
    dialog = UserDialog(ConsoleUserInterface())

    with pytest.raises(InvalidPatientIdException):
        _ = dialog._convert_patient_id('один')

