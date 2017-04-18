from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Column, Date, Float, ForeignKey, Integer, String, Text, text

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name=db.Column(db.String(20))
    student = db.relationship('Student', backref='owner', lazy='dynamic')
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Student(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    user_id = Column(Integer,ForeignKey('user.id'))
    def __init__(self, id, name, uid):
        self.id = id
        self.name = name
        self.uid = uid
def add_user(id,name):
    user = User(id,name)
    db.session.add(user)
    db.session.commit()

def add_student(id,name, uid):
    student = Student(id,name, uid)
    db.session.add(student)
    db.session.commit()

@app.route('/')
def hello_world():
    db.create_all()
    print(db)
    return "hello"
    # add_user(11, 'Nguyen')
    # user = User.query.filter_by(id=10).first()
    # print(user.name)

    # user = User.query.filter_by(name='Nguyen')
    # for x in user:
    #     print(x.id)
    # return 'Hello World!'

    # add_student(20, 'Hoang', 11)

if __name__ == '__main__':
    app.run(debug=True)
