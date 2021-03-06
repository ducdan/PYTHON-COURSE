from flask import Flask,json,render_template,request,redirect
from flask_login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from werkzeug.security import generate_password_hash,check_password_hash
from hashlib import md5

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.secret_key='thisissecretkey'
db=SQLAlchemy(app)
class User(UserMixin,db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    user_name=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)

    def __init__(self,username,password):
        self.user_name=username
        self.setPassword(password)
    def setPassword(self,password):
        self.password=md5(password.encode()).hexdigest()

login_manager=LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=User.query.filter_by(user_name=username,password=md5(password.encode()).hexdigest()).first()
        if user:
            login_user(user=user)
    if(current_user.is_authenticated):
        return redirect('/home')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout success'

@app.route('/home')
@login_required
def home():
    return ('Current user: '+current_user.user_name+
            '\nCurrent password: '+current_user.password)
@app.route('/register',methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    db.session.add(User(username,password))
    db.session.commit()
    return "Registed successful"
@app.route('/')
def hello_world():
    db.create_all()
    # print(md5('123456'.encode()).hexdigest())
    # print(md5('123456'.encode()).hexdigest())
    return redirect('/login')



@app.route('/api/<user_name>/<password>')
def getPassword(user_name,password):
    user = User.query.filter_by(user_name=user_name,password=md5(password.encode()).hexdigest()).first()
    return user.password

@app.route('/user/<user_id>',methods=['POST','PUT'])
def edit(user_id):
    return "User"+user_id
if __name__ == '__main__':
    app.run(debug=True,port=8080)


