from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Text, CHAR, DATE, Float, DECIMAL, DateTime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)



class USER(db.Model):
    ID_USER = Column(Integer, primary_key=True, autoincrement=True)
    USERNAME = Column(String(50), nullable=False)
    PASSWORD = Column(String(50), nullable=False)
    ITEM = db.relationship('ITEM', backref='owner_item_user', lazy='dynamic')
    BID = db.relationship('BID',backref='owner_bid_user', lazy='dynamic')
    def __init__(self,username,password):
        self.USERNAME = username
        self.PASSWORD = password

class ITEM(db.Model):
    ID_ITEM = Column(Integer, primary_key=True, autoincrement=True)
    NAME = Column(String(50), nullable=False)
    DESCRIPTION = Column(String(50), nullable=False)
    START_TIME = Column(String(50))
    ID_OWNER = Column(Integer, ForeignKey('USER.ID_USER'))
    BID_ITEM = db.relationship('BID', backref='owner_bid_item', lazy='dynamic')

    def __init__(self,name,description,owner_id,start_time=None):
        self.NAME = name
        self.DESCRIPTION = description
        self.START_TIME = start_time
        self.ID_OWNER = owner_id


class BID(db.Model):
    ID_BID = Column(Integer, primary_key=True, autoincrement=True)
    PRICE = Column(Float, nullable=False)
    USER_ID = Column(Integer, ForeignKey('USER.ID_USER'))
    ITEM_ID = Column(Integer, ForeignKey('ITEM.ID_ITEM'))
    def __init__(self, price,user_id,item_id):
        self.PRICE = price
        self.USER_ID = user_id
        self.ITEM_ID = item_id

@app.route('/')
def reset():
    print(db)
    db.drop_all()
    db.create_all()

# Add three users to the database

    user1 = USER('tin', '123456')
    user2 = USER('tai', '123')
    user3 = USER('tuan', '1234')
    db.session.add_all([user1, user2, user3])
    db.session.commit()

# Make one user auction a baseball
    baseball = ITEM('baseball', 'ball', user1.ID_USER)
    db.session.add(baseball)
    db.session.commit()

# Have each other user place two bids on the baseball
    bid1 = BID(price=100, user_id=user2.ID_USER, item_id=baseball.ID_ITEM)
    bid2 = BID(price=200, user_id=user3.ID_USER, item_id=baseball.ID_ITEM)
    bid3 = BID(price=300, user_id=user1.ID_USER, item_id=baseball.ID_ITEM)
    db.session.add_all([bid1, bid2, bid3])
    db.session.commit()

# Perform a query to find out which user placed the highest bid
    i = db.session.query(USER.USERNAME, ITEM.NAME, BID.PRICE).join(BID, ITEM).filter(ITEM.NAME == "baseball").order_by(
        BID.PRICE).all()

    highest_bid = i[-1].USERNAME

    print("{} set the highest bid for the {} at ${}".format(highest_bid, i[-1].NAME, i[-1].PRICE))

    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)