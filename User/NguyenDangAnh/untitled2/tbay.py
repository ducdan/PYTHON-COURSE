from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String,Float,DateTime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class user(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    id_bid = Column(Integer, ForeignKey('bid.id'))
    bid = db.relationship('BID', backref='owner_bid_user', lazy='dynamic')
    item = db.relationship('ITEM', backref='owner_item_user', lazy='dynamic')

    def __init__(self, username, password,idbid,iditem):
        self.username = username
        self.password = password

class item(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime)
    bid = db.relationship('BID', backref='owner_bid_item', lazy='dynamic')
    id_user = Column(Integer, ForeignKey('user.id'))

    def __init__(self,id, name, description, start_time,idbid):
        self.id=id
        self.name = name
        self.description = description
        self.start_time = start_time
        self.id_bid=idbid

class bid(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    user = db.relationship('USER', backref='owner_user_bid', lazy='dynamic')
    item = db.relationship('ITEM', backref='owner_item_bid', lazy='dynamic')

    def __init__(self, price):
        self.price = price

def add_user( id,username, password):
    USERS = user( id,username, password)
    db.session.add(USERS)
    db.session.commit()


@app.route('/')
def hello_world():
    print(db)
    db.create_all()

    add_user(1,"danganh","123456")
    add_user(2,"abc","123456")
    add_user(3,"def","123456")

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
