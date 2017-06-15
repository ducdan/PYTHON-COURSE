from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, Integer, String, Text

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class song(Model):
    __tablename__ = "songs"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
