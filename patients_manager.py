from exceptions import PatientNotExistsException, StatusTooLowException


class PatientsManager:
    _ID_OFFSET = 1
    _MIN_STATUS = 0

    _STR_PATIENTS_STATUSES = {
        0: 'Тяжело болен',
        1: 'Болен',
        2: 'Слегка болен',
        3: 'Готов к выписке',
    }

    def __init__(self, patients_base):
        self._patients_base = patients_base

    def get_status(self, patient_id):
        try:
            return self._STR_PATIENTS_STATUSES[self._patients_base[patient_id-self._ID_OFFSET]]
        except IndexError as _:
            raise PatientNotExistsException()

    def status_down(self, patient_id):
        try:
            if self._patients_base[patient_id-self._ID_OFFSET] == self._MIN_STATUS:
                raise StatusTooLowException()
            self._patients_base[patient_id-self._ID_OFFSET] -= 1
        except IndexError as _:
            raise PatientNotExistsException()

    def discharge(self, patient_id):
        try:
            self._patients_base.pop(patient_id-self._ID_OFFSET)
        except IndexError as _:
            raise PatientNotExistsException()