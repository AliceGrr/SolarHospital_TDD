from constants import CommandTypes
from exceptions import InvalidPatientIdException


class UserDialog:
    _COMMANDS = {
        CommandTypes.GET_STATUS: 'показать статус',
        CommandTypes.DISCHARGE: 'выписать',
        CommandTypes.STATUS_DOWN: 'понизить статус',
        CommandTypes.STOP: 'стоп'
    }

    def __init__(self, user_interface):
        self._user_interface = user_interface

    def _convert_patient_id(self, user_input_patient_id):
        try:
            int_patient_id = int(user_input_patient_id)
        except ValueError as _:
            raise InvalidPatientIdException()

        if int_patient_id < 1:
            raise InvalidPatientIdException()
        return int(user_input_patient_id)

    def _convert_command(self, user_input_command):
        lowered_user_input_command = user_input_command.lower()
        for command, user_input in self._COMMANDS.items():
            if lowered_user_input_command == user_input:
                return command
        return CommandTypes.UNKNOWN

    def input_command(self):
        user_input = self._user_interface.input("Введите команду: ")
        return self._convert_command(user_input)

    def input_patient_id(self):
        user_input = self._user_interface.input("Введите id пациента: ")
        return self._convert_patient_id(user_input)

    def print_status(self, patient_status):
        self._user_interface.print(f'Статус пациента: "{patient_status}"')

    def print_status_changed(self, patient_status):
        self._user_interface.print(f'Новый статус пациента: "{patient_status}"')

    def print_patient_discharged(self):
        self._user_interface.print('Пациент выписан')

    def print_message(self, message):
        self._user_interface.print(message)

    def print_stop(self):
        self._user_interface.print('Работа закончена')
