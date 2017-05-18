from flask import Flask,render_template,json


app = Flask(__name__)


@app.route('/')
def hello_world():
    temp=[x for x in  range(10)]
    return render_template('demo.html',temp=temp)


@app.route('/about',methods='GET','POST')
def aboutPage():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

#ten dang nhap su dung post
#con mac dinh dung get