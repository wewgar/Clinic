from flask import render_template, request, redirect, url_for
from .models import Paladin, Pacient

system = Paladin()

doc1 = system.add_doctor(Pacient(1, "Іван Іванов", "ivan@clinic.com"))
system.add_doctor(Pacient(2, "Олена Петрова", "olena@clinic.com"))
system.add_doctor(Pacient(3, "Сергій Сидоров", "sergiy@clinic.com"))
system.add_doctor(Pacient(4, "Наталія Коваленко", "nataliya@clinic.com"))
system.add_doctor(Pacient(5, "Олександр Мельник", "oleksandr@clinic.com"))
system.add_doctor(Pacient(6, "Вікторія Савченко", "viktoriya@clinic.com"))
system.add_doctor(Pacient(7, "Михайло Бондаренко", "mykhailo@clinic.com"))


def index():
    return render_template('index.html')

def doctors():
    return render_template('doctors.html', doctors=system.doctors)

def register(doctor_id):
    doctor = system.get_doctor_by_id(doctor_id)

    if request.method == 'POST':
        patient_name = request.form.get('name')
        patient_email = request.form.get('email')
        appointment_time = request.form.get('time')

        new_patient = Pacient(len(system.pacients) + 1, patient_name, patient_email)
        system.add_pacient(new_patient)

        new_patient.make_appointment(doctor, appointment_time, system)

        return redirect(url_for('appointments'))

    return render_template('register.html', doctor=doctor)

def appointments():
    return render_template('appointments.html', appointments=system.registers)
