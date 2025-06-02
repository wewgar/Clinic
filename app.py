from flask import Flask
import routes 

app = Flask(__name__)

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/doctors', 'doctors', routes.doctors)
app.add_url_rule('/register/<int:doctor_id>', 'register', routes.register, methods=['GET', 'POST'])
app.add_url_rule('/appointments', 'appointments', routes.appointments)

if __name__ == '__main__':
    app.run(debug=True)
