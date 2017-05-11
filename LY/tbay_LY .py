from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tirewnwk:2hvP6oh2WxfbHvVXmZCUygdCnhBhy-Ym@hard-plum.db.elephantsql.com:5432/tirewnwk'
db = SQLAlchemy(app)

class Item(db.Model):
	__tablename__ = 'items'
	
	id = db.Column('item_id', db.Integer, primary_key=True)
	name = db.Column('name', db.String(50), nullable=False)
	description = db.Column('description', db.String(100), nullable=False)
	start_time = db.Column('start_time', db.DateTime)
	
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	
	def __init__(self, name, description, start_time=None, user_id):
		self.name = name
		self.description = description
		if start_time is None:
			self.start_time = datetime.utcnow()
		self.user_id = user_id

class Bid(db.Model):
	__tablename__ = 'bids'
	
	id = db.Column('bid_id', db.Integer, primary_key=True)
	price = db.Column('price', db.Float)
	
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	item_id = db.Column(db.Float, db.ForeignKey('items.id'))
	
	def __init__(self, price, user_id, item_id ):
		self.price = price
		self.user_id = user_id
		self.item_id = item_id
	
class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username', db.String(100), nullable=False)
	password = db.Column('password', db.String(200), nullable=False)
	
	bid_id = db.Relationship('bids', backref = 'bid', lazy='dynamic')
	
	item_id = db.Relationship('items', backref = 'item', lazy='dynamic')
	
	def __init__(self, username, password):
		self.username = username
		self.password = password
	
	
user_1 = User('Anh', 'zKz117')
user_2 = User('Ly', 'VzW427')
user_3 = User('Nam', 'TeH879')

baseball = Item('baseball', 'The best of all time', user_1)

bid_1 = Bid(10, user_2, baseball)
bid_2 = Bid(12, user_2, baseball)
bid_3 = Bid(13, user_3, baseball)
bid_4 = Bid(14, user_3, backball)

