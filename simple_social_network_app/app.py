from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social.db'
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    content = db.Column(db.String(10))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if not request.form['name'] or not request.form['content']:
            flash('Please enter all the fields', 'error')

        else:
            post = Posts(name= request.form['name'], content=request.form['content'])
            db.session.add(post)
            db.session.commit()

    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
