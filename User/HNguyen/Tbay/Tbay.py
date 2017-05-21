from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, desc

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class USER(db.Model):
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    item_user = db.relationship('ITEM', backref='owner_item_user', lazy='dynamic')
    bid_user = db.relationship('BID',backref='owner_bid_user', lazy='dynamic')
    def __init__(self,username,password):
        self.username = username
        self.password = password

class ITEM(db.Model):
    id_item = Column(Integer, primary_key=True, autoincrement=True)
    name_item = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    start_time = Column(String(50))
    user_id = Column(Integer, ForeignKey('USER.id_user'))
    bid_item = db.relationship('BID', backref='owner_bid_item', lazy='dynamic')

    def __init__(self,name_item,description,user_id,start_time=None):
        self.name_item = name_item
        self.description = description
        self.user_id = user_id
        self.start_time = start_time

class BID(db.Model):
    id_bid = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('USER.id_user'))
    item_id = Column(Integer, ForeignKey('ITEM.id_item'))
    def __init__(self, price,user_id,item_id):
        self.price = price
        self.user_id = user_id
        self.item_id = item_id

@app.route('/')
def reset():
    print(db)
    db.drop_all()
    db.create_all()
    user1 = USER(username="Võ", password="74269")
    user2 = USER(username="Hoàng", password="147369456")
    user3 = USER(username="Nguyên", password="147953")
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # Make one user auction a baseball
    baseball = ITEM(name_item="baseball", description="ball", user_id=user1.id_user)
    db.session.add(baseball)
    db.session.commit()

    # Have each other user place two bids on the baseball
    bid1 = BID(price=100, item_id=baseball.id_item, user_id=user2.id_user)
    bid2 = BID(price=200, item_id=baseball.id_item, user_id=user3.id_user)
    db.session.add_all([bid1, bid2])
    db.session.commit()

    # Perform a query to find out which user placed the highest bid
    i = db.session.query(USER.username, ITEM.name_item, BID.price).join(BID, ITEM).filter(ITEM.name_item == "baseball").order_by(
        BID.price).all()

    highest_bidder = i[-1].username

    print("{} set the highest bid for the {} at ${}".format(highest_bidder, i[-1].name_item, i[-1].price))

    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
