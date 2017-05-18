from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Column, Date, Float, ForeignKey, Integer, String, Text, text
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(20))
    student = db.relationship('Student', backref='owner',lazy='dynamic')
    def __init__(self,id,name):
        self.id=id
        self.name=name

def add_user(id,name):
    user = User(id,name)
    db.session.add(user)
    db.session.commit()

class Student(db.Model):
    id= Column (db.Integer,primary_key=True)
    name= Column(db.String(20))
    user_id= Column(Integer,ForeignKey('user.id'))
    def __init__(self, id,name,uid):
        self.id=id
        self.name=name
        self.user_id = uid

def add_student(id,name,uid):
    student = Student(id,name,uid)
    db.session.add(student)
    db.session.commit()

@app.route('/')
def hello_world():
    # add_user(13,'Nga')
    # user=User.query.filter_by(id=10).first()
    # print(user.name)
    add_student(2,'dang anh',10)
    # db.create_all()
    # add_user(10, 'Nguyen')
    # add_user(11, 'anh')
    # add_user(12, 'em')
    return 'Hello World!'
if __name__=='__main__':
    app.run(debug=True)