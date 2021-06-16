from flask import *
import sqlite3

app = Flask(__name__)

@app.before_request
def initdb_command():
    try:
        with sqlite3.connect("Hotel_customer.db") as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, customer text, supplier text, rating INTEGER, comments text)")
            con.commit()
    finally:
        con.close()

@app.route('/')
def index():
    return render_template('index_feedback.html')

@app.route('/submit', methods=['POST'])
def saveDetails():
    if request.method == "POST":
        try:
            customer = request.form['customer']
            supplier = request.form['supplier']
            rating = request.form['rating']
            comments = request.form['comments']
            if not (customer == '' or supplier == ''):
              with sqlite3.connect("Hotel_customer.db") as con:
                 cur = con.cursor()
                 cur.execute("INSERT into feedback (customer, supplier, rating, comments) values (?,?,?,?)", (customer, supplier, rating, comments))
                 con.commit()

        except:
            con.rollback()
            return render_template('index_feedback.html', message='The feedback could not be added for some reason')

        finally:
            if customer == '' or supplier == '':
                return render_template('index_feedback.html', message='Please enter customer and supplier fields')
            else:
              return render_template('success_feedback.html')
              con.close()

if __name__ == '__main__':
    app.run()
