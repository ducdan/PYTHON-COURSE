from flask import Flask,json
from flask.ext.login import LoginManager,UserMixin,login_user,current_user,login_required,logout_user
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

@app.route('/login',methods=['POST','GET'])
def login():
    user=User.query.filter_by(user_name='admin2',password=md5('1234567'.encode()).hexdigest()).first()
    login_user(user=user)
    return 'Login success'

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
@app.route('/register')
def register():
    db.session.add(User('admin2','1234567'))
    db.session.commit()
    return "Registed"
@app.route('/')
def hello_world():
    db.create_all()
    print(md5('123456'.encode()).hexdigest())
    print(md5('123456'.encode()).hexdigest())

    return 'Hello World!'



@app.route('/api/<user_name>/<password>')
def getPassword(user_name,password):
    user = User.query.filter_by(user_name=user_name,password=password).first()
    return json.dumps(user.password)

@app.route('/user/<user_id>',methods=['GET','PUT'])
def edit(user_id):
    return "User"+user_id
if __name__ == '__main__':
    app.run(debug=True,port=8080)


