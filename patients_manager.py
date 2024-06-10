from exceptions import PatientNotExistsException


class PatientsManager:
    _ID_OFFSET = 1

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
        self._patients_base[patient_id-self._ID_OFFSET] -= 1

    def discharge(self, patient_id):
        self._patients_base.pop(patient_id-self._ID_OFFSET)