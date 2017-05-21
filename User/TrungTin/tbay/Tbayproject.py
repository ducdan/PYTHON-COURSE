from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Text, CHAR, DATE, Float, DECIMAL, DateTime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)



Bid_Detail = db.Table('Bid_Detail',
    db.Column('ID_USER', db.Integer, db.ForeignKey('User.ID_USER')),
    db.Column('ID_BID', db.Integer, db.ForeignKey('Bid.ID_BID')))


class User(db.Model):
    __tablename__ = 'User'
    ID_USER = Column(Integer, autoincrement=True, primary_key=True)
    USERNAME = Column(String, nullable=False)
    PASSWORD = Column(String, nullable=False)

    Item = db.relationship("Item", backref="owner_User_Item")
    Bid = db.relationship("Bid",secondary=Bid_Detail, backref="owner_User_Bid")

    def __init__(self, username, password):
        self.USERNAME = username
        self.PASSWORD = password

class Item(db.Model):
    __tablename__ = 'Item'
    ID_ITEMS = Column(Integer, autoincrement=True, primary_key=True)
    NAME = Column(String, nullable=False)
    DESCRIPTION = Column(String, nullable=False)
    START_TIME = Column(DateTime)

    OWNER_ID = Column(Integer, ForeignKey(User.ID_USER), nullable=False)
    BID = db.relationship("Bid", backref="owner_Item_BID")

    def __init__(self, name, des, owner, start_time):
        self.NAME = name
        self.DESCRIPTION= des
        self.START_TIME = start_time



class Bid(db.Model):
    __tablename__ = 'Bid'
    ID_BID = Column(Integer, autoincrement=True, primary_key=True)
    PRICE = Column(Float, nullable=False)

    ITEM_ID = Column(Integer, ForeignKey(Item.ID_ITEMS), nullable=False)


    def __init__(self,price):
        self.PRICE = price



#Add three users to the database

user1 = User('Tin', '123456')
user2 = User('Tai', '654321')
user3 = User('Tuan', '112233')
db.session.add_all([user1,user2,user3])
db.session.commit()


#Make one user auction a baseball
item1 = Item('baseball','ball','18/05/2017',user1.ID_USER)
db.session.add(item1)

#Have each other user place two bids on the baseball
bid1 = Bid(100, item1.ID_ITEMS, user1.ID_USER)
bid2 = Bid(120, item1.ID_ITEMS, user1.ID_USER)
bid3 = Bid(110, item1.ID_ITEMS, user3.ID_USER)
bid4 = Bid(130, item1.ID_ITEMS, user3.ID_USER)
db.session.add_all([bid1,bid2,bid3,bid4])
db.session.commit()

#Perform a query to find out which user placed the highest bid
highest_bid = Bid.query.filter_by(Bid.PRICE.desc()).first
