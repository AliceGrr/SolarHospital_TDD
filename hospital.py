from constants import CommandTypes


class Hospital:
    def __init__(self, hospital_handler, user_dialog):
        self._hospital_handler = hospital_handler
        self._user_dialog = user_dialog

    def start_work(self):
        while True:
            command = self._user_dialog.input_command()
            match command:
                case CommandTypes.GET_STATUS:
                    self._hospital_handler.get_status()
                case CommandTypes.STOP:
                    self._user_dialog.print_stop()
                    break
                case _:
                    break

