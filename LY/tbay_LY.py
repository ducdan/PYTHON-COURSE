from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tirewnwk:2hvP6oh2WxfbHvVXmZCUygdCnhBhy-Ym@hard-plum.db.elephantsql.com:5432/tirewnwk'
db = SQLAlchemy(app)

# Test only
# auction_table = db.Table('auction',
    # db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    # db.Column('item_id', db.Integer, db.ForeignKey('items.id'))) 

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column('id', db.Integer, primary_key=True)
	username = db.Column('username', db.String(100), nullable=False)
	password = db.Column('password', db.String(200), nullable=False)
	
	auction_item = db.relationship('Item', backref='owner', lazy='dynamic')
	
	def __init__(self, username, password):
		self.username = username
		self.password = password

class Item(db.Model):
	__tablename__ = 'items'
	
	id = db.Column('id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(50), nullable=False)
	description = db.Column('description', db.String(100), nullable=False)
	start_time = db.Column('start_time', db.DateTime)
	
	ownwer_id = db.Column('owner_id', db.Integer, db.ForeignKey('users.id'))
	
	def __init__(self, name, description, start_time=None):
		self.name = name
		self.description = description
		if start_time is None:
			self.start_time = datetime.utcnow()		
	
class Bid(db.Model):
	__tablename__ = 'bids'
	
	id = db.Column('bid_id', db.Integer, primary_key=True)
	price = db.Column('price', db.Float)
	
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
	
	items = db.relationship('Item', backref='bids')
	users = db.relationship('User', backref='bids')
	
	def __init__(self, price):
		self.price = price


#Delete all tables from databases and recreate	
#Run first
@app.route('/')
def setting():
	db.drop_all()
	db.create_all()
	return 'Hello'
	
#Run second
@app.route('/run')	
def run():
	# Create three users 
	user_1 = User('Anh', 'zKz117')
	user_2 = User('Ly', 'VzW427')
	user_3 = User('Nam', 'TeH879')
	db.session.add_all([user_1, user_2, user_3])
	
	#One user (user_1) auction baseball
	baseball = Item('baseball', 'The best of all time')
	db.session.add(baseball)
	user_1.auction_item.append(baseball)
	print('Name of the owner: ')
	print(baseball.owner.username)
	
	#User_2 bids
	bid_1 = Bid(10)
	bid_1.items = baseball
	user_2.bids.append(bid_1)
	
	bid_2 = Bid(12)
	bid_2.items = baseball
	user_2.bids.append(bid_2)
	
	#User_3 bids
	bid_3 = Bid(13)
	bid_3.items = baseball
	user_3.bids.append(bid_3)

	bid_4 = Bid(14)
	bid_4.items = baseball
	user_3.bids.append(bid_4)
	
	db.session.add_all([bid_1, bid_2, bid_3, bid_4])
	db.session.commit()
	
	#The highest bid 
	the_best_bid = Bid.query.filter_by(item_id = baseball.id).\
								order_by(Bid.price.desc()).first()
	print('Value of the highest bid: ')							
	print(the_best_bid.price)
	
	return 'running'	
	
if __name__== "__main__":
	app.run(debug=True)	
