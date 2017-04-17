from flask import Flask,render_template,json,request
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('table-demo.html')

@app.route('/querydb',methods=['POST'])
def abcd():
    id=request.form['search']
    dk = request.form['dk']
    db=create_engine('postgres://postgres:123456@localhost/Ex1')
    sql='insert into "Test2" (id) values '+id#from "Test2" where id '+dk+id

    rs=db.execute(sql)
    for x in rs:
        x.items()
    lst=[dict(row.items()) for row in rs]
    print(lst)
    return json.dumps(lst)
if __name__ == '__main__':
    app.run(debug=True)
