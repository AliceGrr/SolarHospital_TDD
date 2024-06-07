from patients_manager import PatientsManager


def test_get_status():
    patients_base = [2, 3, 1, 0]
    worker = PatientsManager(patients_base)

    text_status = worker.get_status(patient_id=2)

    assert text_status == 'Готов к выписке'
    assert worker._patients_base == [2, 3, 1, 0]

def test_status_down():
    patients_base = [2, 3, 1, 0]
    worker = PatientsManager(patients_base)

    worker.status_down(patient_id=2)

    assert worker._patients_base == [2, 2, 1, 0]

def test_discharge():
    patients_base = [2, 3, 1, 0]
    worker = PatientsManager(patients_base)

    worker.discharge(patient_id=2)

    assert worker._patients_base == [2, 1, 0]