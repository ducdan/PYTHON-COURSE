from flask import Flask,render_template,request,send_file
from flask_principal import Principal, Permission, RoleNeed
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Text, CHAR, DATE, Float, DECIMAL

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class NhanVien(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    role = Column(String(50))
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

@app.route('/admin')
def ViewAdmin():
    username = request.form['username']
    nv = NhanVien()
    rs = nv.query.filter_by(name = username)
    for x in rs:
        print(x)
    return 'Success'


if __name__ == '__main__':
    app.run(debug=True)