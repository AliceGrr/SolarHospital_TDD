from exceptions import PatientNotExistsException, InvalidPatientIdException


class HospitalHandler:
    def __init__(self, user_dialog, patients_repository):
        self._user_dialog = user_dialog
        self._patients_repository = patients_repository

    def get_status(self):
        try:
            patient_id = self._user_dialog.input_patient_id()
            status = self._patients_repository.get_status(patient_id)
            self._user_dialog.print_status(status)
        except (PatientNotExistsException, InvalidPatientIdException) as ex:
            self._user_dialog.print_message(ex.message)

    def status_down(self):
        try:
            patient_id = self._user_dialog.input_patient_id()
            self._patients_repository.status_down(patient_id)
            new_status = self._patients_repository.get_status(patient_id)
            self._user_dialog.print_status_changed(new_status)
        except (PatientNotExistsException, InvalidPatientIdException) as ex:
            self._user_dialog.print_message(ex.message)

    def discharge(self):
        try:
            patient_id = self._user_dialog.input_patient_id()
            self._patients_repository.discharge(patient_id)
            self._user_dialog.print_patient_discharged()
        except PatientNotExistsException as ex:
            self._user_dialog.print_message(ex.message)
