from flask import Flask 
from routes import index, doctors, register, appointments

app = Flask(__name__)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/doctors', 'doctors', doctors)
app.add_url_rule('/register/<int:doctor_id>', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/appointments', 'appointments', appointments)

if __name__ == '__main__':
    app.run(debug=True)