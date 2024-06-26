class PatientNotExistsException(Exception):
    message = 'Такого пациента нет в больнице'


class StatusTooLowException(Exception):
    message = 'Статус нельзя понизить (никто не умирает у нас)'


class InvalidPatientIdException(Exception):
    message = 'ID пациента должно быть положительным числом'
