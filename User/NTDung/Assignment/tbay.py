from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, func


db = create_engine('postgres://postgres:12345ad@localhost:5432/tbay')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class User(Base):  # User
    __tablename__ = "users"
    id_user = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    item = relationship("Item", backref="owner_User_Item")
    item = relationship("Bid", backref="owner_User_Bid")

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Item(Base):  # Items
    __tablename__ = "items"
    id_items = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime)

    owner_id = Column(Integer, ForeignKey(User.id_user), nullable=False)
    bid = relationship("Bid", backref="owner_Item_Bid")

    def __init__(self, name, des, owner, start_time=None):
        self.name = name
        self.description = des
        self.owner_id = owner
        self.start_time = start_time

class Bid(Base):  # Bid
    __tablename__ = "bids"
    id_bid = Column(Integer, autoincrement=True, primary_key=True)
    price = Column(Float, nullable=False)

    item_id = Column(Integer, ForeignKey(Item.id_items), nullable=False)
    bidder_id = Column(Integer, ForeignKey(User.id_user), nullable=False)

    def __init__(self, price, item, bidder):
        self.price = price
        self.item_id = item
        self.bidder_id = bidder

Base.metadata.drop_all(bind=db)
Base.metadata.create_all(bind=db)

# 1. Add three user
print('1. Add three user: ')
print('     STT Username    Password')
user1 = User('user1', '123')
user2 = User('user2', 'abc')
user3 = User('user3', 'xyz')
user = [user1, user2, user3]
for u in user:
    session.add(u)
    session.commit()
    print("     {}   {}         {}".format(u.id_user, u.username, u.password))


# 2. Make one user auction a baseball
print('2. Make one user auction a baseball: ')
baseball = Item('baseball', 'A baseball', user1.id_user)
session.add(baseball)
session.commit()
print("     {} make an auction for {}.".format(user1.username, baseball.name))
# 3.  Have each other user place two bids on the baseball
print('3. Have each other user place two bids on the baseball: ')
bid1 = Bid(60, baseball.id_items, user2.id_user)
bid2 = Bid(55, baseball.id_items, user2.id_user)
bid3 = Bid(45, baseball.id_items, user3.id_user)
bid4 = Bid(60, baseball.id_items, user3.id_user)
bid = [bid1, bid2, bid3, bid4]
for b in bid:
    session.add(b)
    session.commit()
    print("     user{} place on the baseball at  {}$.".format(b.bidder_id, b.price))

# 4. Perform a query to find out which user placed the highest bid
print('4. Perform a query to find out which user placed the highest bid: ')
# --- Cách 1 ---:  All users placed the highest bid
highest_price =session.query(func.max(Bid.price))
highest_bid = session.query(Bid).filter_by(price=highest_price).all()
for highest in highest_bid:
    print("     user{} placed the highest bid on the baseball at {}$.".format(highest.bidder_id, highest.price))

# --- Cách 2 ---:   One user placed the highest bid
#highest_bid = session.query(Bid).order_by(Bid.price.desc()).first()
#print("     user{} placed the highest bid on the baseball at {}$".format(highest_bid.bidder_id, highest_bid.price))






