from flask import render_template, request, redirect, url_for
from models import Paladin, Pacient, Doctor

system = Paladin()

doc1 = Doctor(1, "Іван Іванов", "ivan@clinic.com", "Терапевт")
doc2 = Doctor(2, "Олена Петрова", "olena@clinic.com", "Кардіолог")
doc3 = Doctor(3, "Сергій Сидоров", "sergiy@clinic.com", "Хірург")
doc4 = Doctor(4, "Наталія Коваленко", "nataliya@clinic.com", "Педіатр")
doc5 = Doctor(5, "Олександр Мельник", "oleksandr@clinic.com", "Невролог")
doc6 = Doctor(6, "Вікторія Савченко", "viktoriya@clinic.com", "Офтальмолог")
doc7 = Doctor(7, "Михайло Бондаренко", "mykhailo@clinic.com", "Ортопед")

for doc in [doc1, doc2, doc3, doc4, doc5, doc6, doc7]:
    system.add_doctor(doc)

pat1 = Pacient(1, "Марія Петренко", "maria@gmail.com")
system.add_pacient(pat1)

from models import Doctor 

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

        registration = new_patient.make_appointment(
            doctor,
            appointment_time,
            system
        )

        return redirect(url_for('appointments'))

    return render_template('register.html', doctor=doctor)


def appointments():
    return render_template('appointments.html', appointments=system.registers)
