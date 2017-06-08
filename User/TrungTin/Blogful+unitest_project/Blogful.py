from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime

from flask_login import UserMixin, LoginManager, login_required,\
                        login_user, logout_user, current_user

from hashlib import sha256
import datetime
import math
import random

app = Flask(__name__)
app.config.from_object('config.TestConfig')
app.secret_key = '123456'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login_get'
login_manager.login_message = 'danger'

class Entry(db.Model):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, title, content):
        self.title = title
        self.content = content

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = sha256(password.encode('utf-8')).hexdigest()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def add_user():
    db.drop_all()
    db.create_all()
    user1 = User('tin', 'tintin@gmail.com', '123456')
    user2 = User('tai', 'taitai@gmail.com', '1234567')
    admin = User('admin', 'admin@gmail.com', 'admin')
    db.session.add_all([user1, user2, admin])
    db.session.commit()
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name=username).first()

        if (user == None):
            return render_template('login.html')
        elif (sha256(password.encode('utf-8')).hexdigest() == user.password):
            login_user(user=user)
            return redirect('/add-content')
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return render_template('logout.html')

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@app.route('/add-content')
@login_required
def add_content():
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
                reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
o               ccaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    for i in range(25):
        entry = Entry(title="Test Entry #{}".format(i),
                      content=content)
        db.session.add(entry)
    db.session.commit()
    return redirect('/entries/page/1')

entry_per_page = 5
@app.route('/entries/page/<int:page>', methods=['GET', 'POST'])
@login_required
def show_entries(page):
    global entry_per_page # default value = 5

    if (request.method == 'POST'):
        entry_per_page = int(request.form['per_page']) # we can use input form to get data from user
    else:
        pass

    entry_quantity = Entry.query.count() # quantity of entries in table
    if (entry_quantity > entry_per_page):
        page_quantity = int(math.ceil(entry_quantity / entry_per_page))  # round up
    else:
        page_quantity = 1

    start_entry = entry_per_page * (page - 1) # get entry from table
    end_entry = start_entry + entry_per_page


    # if (end_entry < 0): end_entry = 0

    entries = Entry.query.order_by(Entry.datetime.desc())[start_entry:end_entry]

    return render_template('entries.html', entries=entries, entry_per_page=entry_per_page,
                           page_quantity=page_quantity, currentPage=page,notice='Hello, ' + current_user.name)

@app.route('/entries/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    if (request.method == 'POST'):
        title = request.form['title']
        content = request.form['content']
        new_entry = Entry(title, content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/entries/page/1')
    else:
        pass
    return render_template('add-entry.html',
                           notice= 'Add a new post, ' + current_user.name)

@app.route('/entries/<id>', methods=['GET', 'POST'])
@login_required
def view_entry(id):
    entry = Entry.query.filter_by(id=id).first()
    return render_template('view-entry.html',
                           entry=entry, entry_id=id)



@app.route('/entries/<id>/edit', methods=['GET','POST'])
@login_required
def edit_entry(id):
    entry = Entry.query.filter_by(id=id).first()
    if (request.method == 'POST'):
        title = request.form['title']
        content = request.form['content']
        entry.title = title
        entry.content = content
        db.session.add(entry)
        db.session.commit()
        return render_template('view-entry.html',
                               entry=entry, entry_id=id)
    else:
        pass
    return render_template('edit-entry.html', entry=entry)

@app.route('/entries/<id>/delete', methods=['GET', 'POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.filter_by(id=id).first()
    if (request.method == 'POST'):
        if (request.form['submit'] == 'delete'):
            db.session.delete(entry)
            db.session.commit()
            return redirect('/entries/page/1')
        elif (request.form['submit'] == 'cancel'):
            return render_template('view-entry.html',
                                   entry=entry, entry_id=id)
        else:
            pass
    else:
        pass
    return render_template('delete-entry.html',
                           entry=entry, entry_id=id)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)