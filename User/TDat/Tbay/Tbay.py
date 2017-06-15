from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DATE, Float

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User (db.Model):
    __tablename__ = 'Users'
    ID_NAME = Column(Integer, autoincrement=True, primary_key=True)
    USERNAME = Column(String, nullable=False)
    PASSWORD = Column(String, nullable=False)

    def __init__(self, USERNAME, PASSWORD):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD

class Items (db.Model):
    __tablename__ = 'Items'
    ID_ITEMS = Column(Integer, autoincrement = True, primary_key = True)
    NAME = Column(String, nullable=False)
    DESCRIPTION = Column(Text, nullable=False)
    START_TIME = Column(DATE)

    NAME_ID = Column(Integer, ForeignKey(User.ID_NAME))

    def __init__(self, NAME, DESCRIPTION, START_TIME,NAME_ID):
        self.NAME = NAME
        self.DESCRIPTION = DESCRIPTION
        self.START_TIME = START_TIME
        self.NAME_ID = NAME_ID

class Bid (db.Model):
    __tablename__ = 'Bid'
    ID_BID = Column(Integer, autoincrement=True, primary_key=True)
    PRICE = Column(Float, nullable=False)

    ITEMS_ID = Column(Integer, ForeignKey(Items.ID_ITEMS))
    BID_ID = Column(Integer, ForeignKey(User.ID_NAME))

    def __init__(self, PRICE,ITEMS_ID, BID_ID):
        self.PRICE = PRICE
        self.ITEMS_ID = ITEMS_ID
        self.BID_ID= BID_ID

db.drop_all()
db.create_all()
#1
user1 = User('Tín','12345')
user2 = User('Nguyên','54321')
user3 = User('Anh','21221')
user =  [user1, user2, user3]
#2
baseball = Items('Baseball','Sport','18/05/2017', user1.ID_NAME)
db.session.add(baseball)
db.session.commit()
#3
bid1 = Bid('200', baseball.ID_ITEMS, user2.ID_NAME)
bid2 = Bid('250', baseball.ID_ITEMS, user2.ID_NAME)
bid = [bid1, bid2]
for bids in bid:
    db.session.add(bids)
    db.session.commit()
#4
#highest = Bid.query.filter_by(Bid.PRICE.desc()).first

if __name__ == '__main__':
    app.run(debug=True)