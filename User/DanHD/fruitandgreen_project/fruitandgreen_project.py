from flask import Flask,render_template,request

app = Flask(__name__,static_folder='vendors')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/nhapkho')
def nhapkho():
    return render_template('nhapkho.html')

@app.route('/nhap',methods=['POST'])
def nhap():
    fistname=request.form['firstname']
    lastname = request.form['lastname']
    print(fistname+" "+lastname)
    dic={
        'first':fistname,
        'last':lastname
    }
    return render_template('nhapkho.html',fist=dic)
if __name__ == '__main__':
    app.run(debug=True)
