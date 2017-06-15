from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, Integer, String, Text, DateTime, or_
from flask_login import UserMixin, logout_user, login_user, login_required, current_user,LoginManager
from hashlib import sha256
import datetime
import math
import random

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
app.secret_key='thisissecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login_get"
login_manager.login_message_category = "danger"
#---------------------------------------------------
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
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

    def __init__ (self, name, email, password):
        self.name = name
        self.email = email
        self.setpassword = (password)
    def setpassword(self, password):
        self.password = sha256(password.encode('utf-8')).hexdigest()

# -----------------------------------------------------
@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))

#-----------------------------------------------------
@app.route('/')
def add_user():
    db.drop_all()
    db.create_all()
    Nguyen = User("HNguyen","H.Nguyen@gmail.com","nguyen")
    Anh = User("DangAnh","DangAnh@gmail.com","anh")
    Admin = User("admin","Admin@gmail.com","admin")
    db.session.add_all([Anh, Nguyen, Admin])
    db.session.commit()
    return redirect('/login')

#-----------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name=username).first()
        if (user == None):
            return render_template('login.html',
                                   err='Nhập sai, nhập lại!')
        elif (sha256(password.encode('utf-8')).hexdigest() == user.password):
            login_user(user=user)
            return redirect('/entries/page/1')
        else:
            return render_template('login.html')

    return render_template('login.html',
                           err="Register")
#------------------------------------------------------
@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return render_template('logout.html')
#-----------------------------------------------------
@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')
#------------------------------------------------------
@login_required
@app.route('/register', methods=['GET','POST'])
def register():
    if (request.method == 'POST'):
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']

        existence_user = User.query.filter_by(or_(User.name==name, User.email==email)).first()
        if(existence_user == None ):
            user = User(name,email,password)
            db.session.add(user)
            db.session.commit()
            return  redirect('/login')
        else:
            return render_template('login.html')
    return render_template('login.html')


#-----------------------------------------------------
@app.route('/add-entries')
def seed():
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    for i in range(25):
        entry = Entry(title="Test Entry #{}".format(i), content=content)
        db.session.add(entry)
        db.session.commit()
        return redirect('/entries/page/1')
#------------------------------------------------------
entry_per_page = 5
@app.route('/entries/page/<int:page>', methods=['GET', 'POST'])
@login_required
def show_entries(page):
    global entry_per_page

    if (request.method == 'POST'):
        entry_per_page = int(request.form['per_page'])
    else:
        pass

    entry_quantity = Entry.query.count()
    if (entry_quantity > entry_per_page):
        page_quantity = int(math.ceil(entry_quantity / entry_per_page))
    else:
        page_quantity = 1

    start_entry = entry_per_page * (page - 1)
    end_entry = start_entry + entry_per_page


    entries = Entry.query.order_by(Entry.datetime.desc())[start_entry:end_entry]

    return render_template('entries.html', entries=entries, entry_per_page=entry_per_page,
                           page_quantity=page_quantity, currentPage=page)
#---------------------------------------------------------
@app.route('/entries/add', methods=['GET', 'POST'])
@login_required
def add_entries():
    if (request.method == 'POST'):
        title = request.form['title']
        content = request.form['content']
        new_entries = Entry(title, content)
        db.session.add(new_entries)
        db.session.commit()
        return redirect('/entries/page/1')
    else:
        pass
    return render_template('add-entries.html', + current_user.name)

@app.route('/entries/<id>', methods=['GET', 'POST'])
@login_required
def view_entries(id):
    entries = Entry.query.filter_by(id=id).first()
    return render_template('view.html',
                           entry=entries, entry_id=id)

@app.route('/entries/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit_entries(id):
    entries = Entry.query.filter_by(id=id).first()
    if (request.method == 'POST'):
        title = request.form['title']
        content = request.form['content']
        entries.title = title
        entries.content = content
        db.session.add(entries)
        db.session.commit()
        return render_template('view.html',
                               entry=entries, entry_id=id)
    else:
        pass
    return render_template('edit-entries.html', entry=entries)

@app.route('/entries/<id>/delete', methods=['GET', 'POST'])
@login_required
def delete_entries(id):
    entries = Entry.query.filter_by(id=id).first()
    if (request.method == 'POST'):
        if (request.form['submit'] == 'delete'):
            db.session.delete(entries)
            db.session.commit()
            return redirect('/entries/page/1')
        elif (request.form['submit'] == 'cancel'):
            return render_template('view.html',
                                   entry=entries, entry_id=id)
        else:
            pass
    else:
        pass
    return render_template('delete-entries.html',
                           entry=entries, entry_id=id)
if __name__ == '__main__':
    app.run(debug=True)