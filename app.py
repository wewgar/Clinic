from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"

class Pacient(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.registrations = []

    def make_appointment(self, doctor, time, system):
        registration = Register(self, doctor, time)
        system.add_register(registration)
        self.registrations.append(registration)
        doctor.register.append(registration)
        return registration

class Doctor(User):
    def __init__(self, user_id, name, email, specialty):
        super().__init__(user_id, name, email)
        self.specialty = specialty
        self.register = []

    def __str__(self):
        return f"Dr. {self.name}, {self.specialty}"

class Register:
    def __init__(self, pacient, doctor, time):
        self.pacient = pacient
        self.doctor = doctor
        self.time = time

    def __str__(self):
        return f"{self.time} - {self.pacient.name} у {self.doctor.name}"

class Paladin:
    def __init__(self):
        self.pacients = []
        self.doctors = []
        self.registers = []

    def add_pacient(self, pacient):
        self.pacients.append(pacient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_register(self, register):
        self.registers.append(register)

    def get_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.user_id == int(doctor_id):
                return doctor
        return None


system = Paladin()

doc1 = Doctor(1, "Іван Іванов", "ivan@clinic.com", "Терапевт")
doc2 = Doctor(2, "Олена Петрова", "olena@clinic.com", "Кардіолог")
doc3 = Doctor(3, "Сергій Сидоров", "sergiy@clinic.com", "Хірург")
doc4 = Doctor(4, "Наталія Коваленко", "nataliya@clinic.com", "Педіатр")
doc5 = Doctor(5, "Олександр Мельник", "oleksandr@clinic.com", "Невролог")
doc6 = Doctor(6, "Вікторія Савченко", "viktoriya@clinic.com", "Офтальмолог")
doc7 = Doctor(7, "Михайло Бондаренко", "mykhailo@clinic.com", "Ортопед")

system.add_doctor(doc1)
system.add_doctor(doc2)
system.add_doctor(doc3)
system.add_doctor(doc4)
system.add_doctor(doc5)
system.add_doctor(doc6)
system.add_doctor(doc7)

pat1 = Pacient(1, "Марія Петренко", "maria@gmail.com")
system.add_pacient(pat1)