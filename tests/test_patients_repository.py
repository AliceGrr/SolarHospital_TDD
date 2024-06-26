import pytest

from exceptions import PatientNotExistsException, StatusTooLowException
from patients_repository import PatientsRepository


def test_get_status():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    text_status = worker.get_status(patient_id=2)

    assert text_status == 'Готов к выписке'
    assert worker._patients_base == [2, 3, 1, 0]


def test_get_status_when_patient_not_exists():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        _ = worker.get_status(patient_id=99)


def test_get_status_when_empty_patients_base():
    patients_base = []
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        _ = worker.get_status(patient_id=1)


def test_status_down():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    worker.status_down(patient_id=2)

    assert worker._patients_base == [2, 2, 1, 0]


def test_status_down_when_patient_not_exists():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        worker.status_down(patient_id=99)


def test_status_down_when_empty_patients_base():
    patients_base = []
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        worker.status_down(patient_id=1)


def test_status_down_when_patient_status_minimum():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    with pytest.raises(StatusTooLowException):
        worker.status_down(patient_id=4)


def test_discharge():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    worker.discharge(patient_id=2)

    assert worker._patients_base == [2, 1, 0]


def test_discharge_when_patient_not_exists():
    patients_base = [2, 3, 1, 0]
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        worker.discharge(patient_id=99)

    assert worker._patients_base == [2, 3, 1, 0]


def test_discharge_when_empty_patients_base():
    patients_base = []
    worker = PatientsRepository(patients_base)

    with pytest.raises(PatientNotExistsException):
        worker.discharge(patient_id=1)
