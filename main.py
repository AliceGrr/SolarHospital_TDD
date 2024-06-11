from console_user_interface import ConsoleUserInterface
from hospital import Hospital
from hospital_handler import HospitalHandler
from patients_repository import PatientsRepository
from user_dialog import UserDialog

patients_repository = PatientsRepository([2, 3, 1, 0])
user_dialog = UserDialog(ConsoleUserInterface())
hospital_handler = HospitalHandler(user_dialog, patients_repository)
hospital = Hospital(hospital_handler, user_dialog)

hospital.start_work()
