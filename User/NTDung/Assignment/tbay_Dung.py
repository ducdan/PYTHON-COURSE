from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, func

db = create_engine('postgres://postgres:12345ad@localhost:5432/tbay')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class User(Base):  # User
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    item = relationship("Item", backref="owner_User_Item")
    asso = relationship("Association", backref="owner_User_Association")

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
    id_bid = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    item_id = Column(Integer, ForeignKey(Item.id_items), nullable=False)
    asso = relationship("Association", backref="owner_Bid_Association")

    def __init__(self, price, item):
        self.price = price
        self.item_id = item


class Association(Base):
    __tablename__ = 'association'
    id_asso = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id_user), nullable=False)
    bid_id = Column(Integer, ForeignKey(Bid.id_bid), nullable=False)

    def __init__(self, user, bid):
        self.user_id = user
        self.bid_id = bid



Base.metadata.drop_all(bind=db)
Base.metadata.create_all(bind=db)

# 1. Add three user
print('1. Add three user: ')
print('     STT Username    Password')
user1 = User('Dung', '123')
user2 = User('Lam', 'abc')
user3 = User('Duyen', 'xyz')
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
bid1 = Bid(60, baseball.id_items)
bid2 = Bid(55, baseball.id_items)
bid3 = Bid(50, baseball.id_items)
session.add_all([bid1, bid2, bid3])
session.commit()

asso1 = Association(user2.id_user, bid1.id_bid)
asso2 = Association(user3.id_user, bid1.id_bid)
asso3 = Association(user2.id_user, bid2.id_bid)
asso4 = Association(user3.id_user, bid3.id_bid)
session.add_all([asso1, asso2, asso3, asso4])
session.commit()

bids = session.query(Association).join(Bid, Association.bid_id == Bid.id_bid)\
        .join(User, User.id_user == Association.user_id)\
        .join(Item, Item.id_items == Bid.item_id)\
        .add_column(User.username).add_column(Bid.price).add_column(Item.name).all()

for b in bids:
    print("     {} place on the {} at  {}$.".format(b.username, b.name, b.price))

# 4. Perform a query to find out which user placed the highest bid
print('4. Perform a query to find out which user placed the highest bid: ')
# --- Cách 1 ---:  All users placed the highest bid
# highest_price = session.query(func.max(Bid.price))
# highest_bid = session.query(Association).join(Bid, Association.bid_id == Bid.id_bid)\
#                 .join(User, User.id_user == Association.user_id)\
#                 .add_column(Bid.price)\
#                 .add_column(User.username)\
#                 .filter(Bid.price == highest_price).all()
#
# for highest in highest_bid:
#     print("     {} placed the highest bid on the baseball at {}$.".format(highest.username, highest.price))

# --- Cách 2 ---:   One user placed the highest bid
highest_bid = session.query(Association).join(Bid, Association.bid_id == Bid.id_bid)\
                .join(User, User.id_user == Association.user_id)\
                .add_column(Bid.price)\
                .add_column(User.username)\
                .order_by(Bid.price.desc()).first()
print("     {} placed the highest bid at {}$.".format(highest_bid.username, highest_bid.price))






