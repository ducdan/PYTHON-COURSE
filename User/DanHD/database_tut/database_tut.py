from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Column, Date, Float, ForeignKey, Integer, String, Text, text
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db=SQLAlchemy(app)


class Xnk(db.Model):
    __tablename__ = 'xnk'

    id = Column(db.Integer, db.Sequence('user_id'),primary_key=True)
    mapn = Column(Integer)
    ncc = Column(Text)
    nguoinhan = Column(Text)
    ngaynhap = Column(Date)
    diadiemnhan = Column(Text)
    sltheoct = Column(Float)
    slthucnhap = Column(Float)
    tensp = Column(Text)
    container = Column(String(15))
    donvitinh = Column(String(10))
    sl = Column(Float)
    note = Column(Text)
    mapx = Column(Integer)
    tenkh = Column(Text)
    nguoigiao = Column(Text)
    ngaygiao = Column(Date)
    diadiemgiao = Column(Text)
    sltheoyc = Column(Float)
    slthucxuat = Column(Float)

class Kho(db.Model):
    __tablename__ = 'kho'

    makho = Column(String(5), primary_key=True)
    ten = Column(Text)
    diachi = Column(Text)
    sdt = Column(String(15))
    thukho = Column(Text)
    tenloaisp = Column(Text)
    tensp = Column(Text)
    kichthuoc = Column(Integer)
    donvitinh = Column(String(10))
    slton = Column(Float)
    sltthucte = Column(Float)


class User(db.Model):
    id=db.Column(db.Integer,db.Sequence('user_id'),primary_key=True)
    name=db.Column(db.String(20))
    student = db.relationship('Student',backref='owner',lazy='dynamic')
    def __init__(self,name):
        self.name=name

class Student(db.Model):
    id=Column(Integer,primary_key=True)
    name=Column(String(20))
    user_id=Column(Integer,ForeignKey('user.id'))
    def __init__(self,id,name,uid):
        self.id=id
        self.name=name
        self.user_id=uid
def adduser(name):
    user = User( name)
    db.session.add(user)
    db.session.commit()
def addstudent(id,name,uid):
    student = Student(id, name,uid)
    db.session.add(student)
    db.session.commit()
@app.route('/')
def hello_world():
    # adduser(13,'Nga')
    # user=User.query.filter_by(name='Nga')
    student =Student.query.all()
    user=User.query.filter_by(id=10)
    # kho=Kho.query.all()
    # for x in kho:
    #     print(x.id)
    # db.create_all()
    # print(db)
    # addstudent(2,'Thanh',10)
    # for x in range(20):
    #     adduser('Hau')
    return render_template('index.html',stu=student)


if __name__ == '__main__':
    app.run(debug=True)
