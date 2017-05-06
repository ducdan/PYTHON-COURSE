from flask import Flask,render_template,request,send_file
from DataModel import KHO, XNK

app = Flask(__name__,static_folder='vendors')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/xemct')
def xemct():
    return render_template('XemCT.html')

@app.route('/xemhangton')
def xemhangton():
    return render_template('xemhangton.html')

@app.route('/xuatkho')
def xuatkho():
    return render_template('xuatkho.html')

@app.route('/phieunhap')
def phieunhap():
    return render_template('phieunhap.html')
@app.route('/phieuxuat')
def phieuxuat():
    return render_template('phieuxuat.html')

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

@app.route('/xemct', methods=['GET', 'POST'])
def show_kho():
    xnk = ""
    MaKho = ""
    LoaiSp = ""
    if request.method == 'POST':
        xnk = request.form['XNK']
        Port_of_Discharge = xnk['']
        Shipper = request.form['LoaiSP']
    data = []
    if ((xnk == "Tất cả") & (Port_of_Discharge == "") & (Shipper == "")):
        data = KHO.query.all()
    elif ((xnk == "Tất cả") & (Port_of_Discharge == "")):
        pass
    elif ((xnk == "Tất cả") & (Shipper == "")):
        pass
    elif ((xnk == "Tất cả")):
        pass
    elif ((Port_of_Discharge == "") & (Shipper == "")):
        data = XNK.query.filter_by(XNK=Port_of_Discharge).all()
    elif ((Port_of_Discharge == "")):
        pass
    elif ((Shipper == "")):
        pass
    else:
        pass

    return render_template("XemCT.html", data = data)

@app.route('/report')
def report():
    return send_file('report.pdf',attachment_filename=True)


if __name__ == '__main__':
    app.run(debug=True)
