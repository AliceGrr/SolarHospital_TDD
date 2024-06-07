import unittest.mock

from console_user_interface import ConsoleUserInterface
from user_dialog import UserDialog


@unittest.mock.patch('builtins.input', side_effect=['показать статус'])
def test_request_command_get_status(_):
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog.request_command()

    assert command == 'get_status'


@unittest.mock.patch('builtins.input', side_effect=['1'])
def test_request_id(_):
    dialog = UserDialog(ConsoleUserInterface())

    patient_id = dialog.request_patient_id()

    assert patient_id == 1


def test_convert_command_get_status():
    dialog = UserDialog(ConsoleUserInterface())

    command = dialog._convert_command('показать статус')

    assert command == 'get_status'


def test_convert_patient_id():
    dialog = UserDialog(ConsoleUserInterface())

    patient_id = dialog._convert_patient_id('1')

    assert patient_id == 1
