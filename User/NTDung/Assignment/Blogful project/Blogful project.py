from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime
from flask.ext.login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user


app = Flask(__name__)
app.config.from_pyfile("config_me.cfg")
app.secret_key = 'thisissecretkey'
db = SQLAlchemy(app)

# Create the model
class Entry(db.Model):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, title, content):
        self.title = title
        self.content = content

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
db.drop_all()
db.create_all()

# Add some data
def seed():
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    for i in range(25):
        entry = Entry(
            title="Test Entry #{}".format(i),
            content=content
        )
        db.session.add(entry)
    db.session.commit()

seed()

#------------------------------
# Setting up the login system
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_get"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))

@app.route('/register')
def register():
    db.session.add(User('admin', '123@gmail.com', '123456'))
    db.session.commit()
    return "Register"

@app.route('/login')
def login():
    user = db.session.query(User).filter_by(name='admin', password='123456').first()
    print(user.name)
    login_user(user=user)
    return 'Login Success'

@app.route('/logout')
@login_required  # check da login moi chay
def logout():
    logout_user()
    return 'Logout success'



# Display the entries
@app.route("/")
@login_required
def entries():
    entries = db.session.query(Entry).order_by(Entry.datetime.desc()).all()
    return render_template("entries.html", entries=entries)

# Add blog entries
@app.route("/entry/<id>")
@login_required
def viewEntry(id):
    entries = db.session.query(Entry).filter_by(id=id).all()
    return render_template("render_entry.html", entries=entries)

@app.route("/entry/<id>/edit")
@login_required
def editEntry(id):
    entry = db.session.query(Entry).filter_by(id=id).first()
    if (entry != None):
        return "Id đã tồn tại!"
    else:
        if (request.method == 'POST'):
            title = request.form['Title']
            content = request.form['Content']

            entry = Entry(title, content)
            db.session.add(entry)
            db.session.commit()
            return render_template("add_entry.html", entries=entries)

@app.route("/entry/<id>/delete")
@login_required
def editEntry(id):
    entry = db.session.query(Entry).filter_by(id=id).first()
    if (entry == None):
        return "Không tồn tại id này!"
    else:
        if (request.method == 'POST'):
            title = request.form['Title']
            content = request.form['Content']

            entry = Entry(title, content)
            db.session.add(entry)
            db.session.commit()
            return render_template("add_entry.html", entries=entries)



if __name__ == '__main__':
    app.run(debug=True)
