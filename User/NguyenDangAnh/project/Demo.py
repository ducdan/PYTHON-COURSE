from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String,Float,DateTime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

association_table = db.Table('association',
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('bids_id', Integer, ForeignKey('bids.id'))
)

class user(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    bid = db.relationship(
        "Bid",
        secondary=association_table,
        back_populates="user")
    item = db.relationship('Item', backref='owner_item_user', lazy='dynamic')


    def __init__(self, username, password):
        self.username = username
        self.password = password

class item(db.Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime)

    id_user = Column(Integer, ForeignKey('users.id'))
    bid = db.relationship('Bid', back_populates='owner_bid_item', lazy='dynamic')

    def __init__(self, name, description, start_time):
        self.id=id
        self.name = name
        self.description = description
        self.start_time = start_time

class bid(db.Model):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    user = db.relationship(
        "User",
        secondary=association_table,
        back_populates="bid")
    id_item = db.Column( db.Integer, db.ForeignKey('id.items'))
    def __init__(self, price):
        self.price = price

def hello_world():
    print(db)
    db.create_all()
    user1 = user(username="nguyen dang anh 1", password="123456")
    user2 = user(username="nguyen dang anh 2", password="123456")
    user3 = user(username="nguyen dang anh 3", password="123456")
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    baseball = item(name="baseball", description="ball", id_user=user1.id)
    db.session.add(baseball)
    db.session.commit()

    bid1 = bid(price=100, id_item=baseball.id, user_id=user2.id)
    bid2 = bid(price=200, id_item=baseball.id, user_id=user3.id)
    db.session.add_all([bid1, bid2])
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
