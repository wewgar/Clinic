from models import Paladin, Doctor, Pacient, Register
from routes import index, doctors, register, appointments

system = Paladin()

system.add_doctor(Doctor(1, "Іван Іванов", "ivan@clinic.com", "Терапевт"))
system.add_doctor(Doctor(2, "Олена Петрова", "olena@clinic.com", "Кардіолог"))
system.add_doctor(Doctor(3, "Сергій Сидоров", "sergiy@clinic.com", "Хірург"))
system.add_doctor(Doctor(4, "Наталія Коваленко", "nataliya@clinic.com", "Педіатр"))
system.add_doctor(Doctor(5, "Олександр Мельник", "oleksandr@clinic.com", "Невролог"))
system.add_doctor(Doctor(6, "Вікторія Савченко", "viktoriya@clinic.com", "Офтальмолог"))
system.add_doctor(Doctor(7, "Михайло Бондаренко", "mykhailo@clinic.com", "Ортопед"))
