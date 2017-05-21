from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'usertbl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    # Create relationship to item. 1 user auction many items.
#######     auction_items = relationship('Item', back_populates='auctioner')
    # Create 1-to-many relationship. 1 user may put many bids 
    have_bids = relationship('transaction', back_populates="col_user")
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Item4bid(db.Model):
    __tablename__ = 'itemtbl'
    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime)
    auctioner_id = Column(Integer, ForeignKey('usertbl.id'))
    # create relationship to user. Many items are auctioned by 1 user
    auctioner = relationship('User', backref="auction_items")
    # create relationship to bid. 1 item has many bids
#     in_bids = relationship('Bid', backref=backref('of_item',uselist=True)) 
    in_bids = relationship('Bid', backref='of_item') 
    def __init__(self, name, description, start_time):
        self.name = name
        self.description = description
        self.start_time = start_time

class Bid(db.Model):
    __tablename__ = 'bidtbl'
    id = Column(Integer,primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    item_id = Column(Integer, ForeignKey('itemtbl.id'))
########     of_item = relationship('Item4bid', back_populates='in_bids') # defined in backref
    # Create 1-many relationship. 1 bid may be put out by many bidders
    bidders = relationship('transaction', back_populates="col_bid")
    def __init__(self, price):
        self.price = price

class transaction(db.Model):
    __tablename__ = 'association'
    user_id = Column(Integer, ForeignKey('usertbl.id'),primary_key=True)
    bid_id = Column(Integer, ForeignKey('bidtbl.id'),primary_key=True)
    # many-to-many relationship of (user table, bid table)
    col_bid = relationship('Bid', back_populates='bidders')
    col_user = relationship('User', back_populates='have_bids')
@app.route('/')
def hello_world():

    db.create_all()
    mai = User("Mai", "pw1")
    hoa = User("Hoa", "pw2")
    anh = User("Anh", "pw3")
    ball = Item4bid("baseball", "a ball sold by Mai", func.now())
    ball1 = Item4bid(name="basketball", description="another ball sold by Mai", start_time=func.now())
    ball.auctioner=mai
    mai.auction_items.append(ball1)
      
    b1 = Bid(200)  
    b1.of_item = ball
    b2 = Bid(300)
    b2.of_item = ball
    b3 = Bid(250)
    b3.of_item = ball
    b4=Bid(500)
    b4.of_item = ball
    b5=Bid(20)
    b6=Bid(30)
    ball1.in_bids.append(b5)
    ball1.in_bids.append(b6)
     
    tran1 = transaction(col_user=hoa, col_bid=b1)
    tran2 = transaction()
    tran2.col_bid = b1
    tran2.col_user = anh
    tran3 = transaction()
    tran3.col_bid=b2
    hoa.have_bids.append(tran3)
    tran4 = transaction()
    tran4.col_user = anh
    b3.bidders.append(tran4)
    tran5 = transaction(col_user=anh, col_bid=b4)
    tran6 = transaction(col_user=hoa, col_bid=b5)
    tran7 = transaction(col_user=anh, col_bid=b6)
    
    db.session.add_all([mai, hoa, anh])      
    db.session.commit()

####################### Try some queries for user-item relationship
    print("querry all users", User.query.all())
    print("query all items", Item4bid.query.all())
    print("who auction what")
    for person in User.query.all():
        for item in person.auction_items:
            print("%s auction %s" %(person.username, item.name))
    print("what are auctioned by whom")        
    for item in Item4bid.query.all():
        print("%s is auctioned by %s." %(item.name, item.auctioner.username))
     
    print("Items Mai autioned:")
    for item in  User.query.filter_by(username ="Mai").first().auction_items:
        print(item.name)


######################### Try some other queries for item-bid relationship

    for item in Item4bid.query.all():
        print("Item %s has %d bids" %(item.name, len(item.in_bids)))
        for bid in item.in_bids:
            print ("%s bids" %bid.price )
    for bid in bid.query.all():
        print ("Bid item %s with price %f" %(bid.of_item.name, bid.price))

######################## Try query m-n table between user-bid             

    print(User.query.filter(User.have_bids.contains(b1)).all())
    print("What items each user bid?")
#     print(hoa.query.filter(hoa.have_bids.any(b2)).all())
#     print(anh.query.filter(anh.have_bids.item_id==1))
    # print (User.query.filter_by(User.bid_id.any(bid.price)).all())
    print("who is the winning bid of each item at what price?")



    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
