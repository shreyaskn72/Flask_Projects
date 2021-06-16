from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    contact = db.Column(db.String(50))
    pin = db.Column(db.Text)


@app.route('/')
def student():
    return render_template('student.html')

@app.route('/success', methods = ['POST'])
def success():
    if not request.form['name'] or not request.form['email'] or not request.form['contact']:
        return 'Please enter all the fields'
    else:
        result = request.form # result_info.html is written in dictionary format with looping.
        student_record= Student(name=request.form['name'], email=request.form['email'], contact=request.form['contact'], pin=request.form['pin'])
        db.session.add(student_record)
        db.session.commit()
        return render_template("result_info.html", result=result)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
