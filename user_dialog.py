from exceptions import InvalidPatientIdException


class UserDialog:
    _COMMANDS = {
        'get_status': 'показать статус',
        'discharge': 'выписать',
        'status_down': 'понизить статус'
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
        for command, user_input in self._COMMANDS.items():
            if user_input_command == user_input:
                return command
        return 'unknown'

    def request_command(self):
        user_input = self._user_interface.input("Введите команду: ")
        return self._convert_command(user_input)

    def request_patient_id(self):
        user_input = self._user_interface.input("Введите id пациента: ")
        return self._convert_patient_id(user_input)

