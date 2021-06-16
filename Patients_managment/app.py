from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.sqlite3'
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)

class Patients(db.Model):
    id = db.Column('patient_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.String(200))
    blood_group = db.Column(db.String(50))
    infection = db.Column(db.String(10))

    def __init__(self, name, age, blood_group, infection):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.infection = infection


@app.route('/')
def list_patients():
    return render_template('list_patients.html', Patients=Patients.query.all())


@app.route('/add', methods=['GET', 'POST'])
def addPatients():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['age'] or not request.form['blood_group']:
            flash('Please enter all the fields', 'error')
        else:
            patient = Patients(request.form['name'], request.form['age'],
                                      request.form['blood_group'], request.form['infection'])

            db.session.add(patient)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('list_patients'))
    return render_template('add_patients.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
