from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'

db = SQLAlchemy(app)
class Mypost(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    topic = db.Column(db.String(100))
    subtopic = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    posts = Mypost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Mypost.query.filter_by(id=post_id).one()    #querying the database
    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods = ['POST'])
def addpost():
    if not request.form['topic'] or not request.form['subtopic'] or not request.form['author'] or not request.form['content']:
        return 'Please enter all the fields'
    else:
        topic = request.form['topic']
        subtopic = request.form['subtopic']
        author = request.form['author']
        content = request.form['content']
        post= Mypost(topic= topic, subtopic=subtopic, author=author, date_posted=datetime.now(), content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
