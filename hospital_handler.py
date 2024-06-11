class HospitalHandler:
    def __init__(self, user_dialog, patients_repository):
        self._user_dialog = user_dialog
        self._patients_repository = patients_repository

    def get_status(self):
        patient_id = self._user_dialog.input_patient_id()
        status = self._patients_repository.get_status(patient_id)
        self._user_dialog.print_status(status)

    def status_down(self):
        patient_id = self._user_dialog.input_patient_id()
        self._patients_repository.status_down(patient_id)
        new_status = self._patients_repository.get_status(patient_id)
        self._user_dialog.print_status_changed(new_status)

    def discharge(self):
        patient_id = self._user_dialog.input_patient_id()
        self._patients_repository.discharge(patient_id)
        self._user_dialog.print_patient_discharged()
