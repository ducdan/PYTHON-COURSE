from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user
from sqlalchemy import Column, Integer, String, Text, DateTime
import datetime
app = Flask(__name__)
app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)

class Entry(db.Model):
    '''
    Content of a post in blog
    '''
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    content = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, title, content):
        '''
        Constructor
        '''
        self.title = title
        self.content = content

class User(db.Model, UserMixin):
    '''
    users that can access the blog
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

    def __init__(self, name, email, password):
        '''
        Constructor
        '''
        self.name = name
        self.email = email
        #self.password = sha256(password.encode('utf-8')).hexdigest()
        self.password = password

def seed(): 
    content = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, \
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt \
    mollit anim id est laborum.""" 
    for i in range(25): 
        entry = Entry( title="Test Entry #{}".format(i), content = content )
        db.session.add(entry)    
    user1 = User(name="user1",email="user1@blog",password="1")
    user2 = User(name="user2",email="user2@blog",password="2")
    user3 = User(name="user3",email="user3@blog",password="3")
    db.session.add_all([user1,user2,user3])
    db.session.commit()
    
login_manager=LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)

@app.route("/")
def home():
    db.drop_all()
    db.create_all()
    seed()
    return redirect("login")

@app.route("/add", methods = ["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        title=request.form["title"]
        content=request.form["content"]
        post = Entry(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return render_template("view.html", post=post)
    return render_template("add.html")

@app.route("/entry/<id>")
@login_required
def view_1_entry(id):
    post = Entry.query.filter_by(id = id).first()
    return render_template("view.html", post = post)

@app.route("/entry/<id>/edit", methods = ["GET", "POST"])
@login_required
def edit_1_entry(id):
    post = Entry.query.filter_by(id = id).first()
    if (request.method == 'POST'):
        title = request.form['title']
        content = request.form['content']
        post.title = title
        post.content = content
        db.session.add(post)
        db.session.commit()
        return redirect('entry/%s' %id)
    return render_template("edit.html", post = post)

@app.route("/entry/<id>/delete")
@login_required
def del_1_entry(id):
    Entry.query.filter_by(id = id).delete()
    db.session.commit()
    entries = db.session.query(Entry) 
    entries = entries.order_by(Entry.datetime.desc()) 
    entries = entries.all()
    return redirect('entries/page/1')

page_len = 5  
@app.route("/entries/page/<int:page>", methods=['GET', 'POST']) 
@login_required
def entries(page):  
    global page_len 
    total_entries = Entry.query.count()
    if (request.method == 'POST'):
        page_len = int(request.form['per_page'])
    entries = db.session.query(Entry) 
    entries = entries.order_by(Entry.datetime.desc()) 
    div_func = lambda entries, count: [entries[i:i+count] for i in range(0, total_entries-1, count)]
    chunks = div_func(entries,page_len)
    return render_template("entries.html", chunks=chunks, page=page) 

@app.route("/login", methods = ["GET", "POST"]) 
def login():
    if request.method == "POST":
        username = request.form["username"] 
        password = request.form["password"]
        user = User.query.filter_by(name=username).first()
        if user and password == user.password :
            login_user(user=user)
            return redirect('entries/page/1')
        else:
            return render_template("login.html", err = "wrong username or password. Please try again.")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout success'

@login_manager.unauthorized_handler  # redirect to login.html if user hasn't been login
def unauthorized():
    return redirect('/login')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)  