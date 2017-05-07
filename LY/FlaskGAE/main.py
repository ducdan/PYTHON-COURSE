from flask import Flask,render_template,request,send_file,redirect
from flask_sqlalchemy import SQLAlchemy
# from requests import Session,cookies
from sqlalchemy import Column,Integer,Text,String,DATE,DECIMAL,Float,CHAR, func

app = Flask(__name__,static_folder='vendors')
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def login():
    print(request.method)
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if (username.lower() == 'admin') and (password == "admin"):
            response = app.make_response(redirect('/home'))
            # response=
            response.set_cookie('user_name',value=username)
            print('set cookies')
            return response
        else: render_template('login.html',err='Bạn đã nhập sai username hoặc password')
    print(request.cookies)
    print(request.cookies.get('user_name'))
    if('admin' in request.cookies):
        print('Here')
    if('user_name' in request.cookies and request.cookies['user_name']=='admin'):
        return redirect('/home')
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    response=redirect('/')
    response.set_cookie('user_name','')
    return response

@app.route('/home')
def main():
    db.create_all()
    print(request.cookies.get('user_name'))
    return render_template('index.html')

@app.route('/comingsoon')
def commingsoon():
    return render_template('comingsoon.html')

class PHIEUNHAP(db.Model):  # Phiếu nhập
    ID_PN = Column(Integer, autoincrement=True, primary_key=True)
    MAPN = Column(CHAR(7), nullable=False)
    SANPHAM = Column(String(50))
    SLNHAP = Column(Float)
    SLNTHUC = Column(Float)
    DVT = Column(String(20))
    CONTAINER_NO = Column(String(20))
    NGAYNHAP = Column(String(20))
    PRICE = Column(Float)
    TONGTIEN = Column(Float)

    def __init__(self, MAPN, SANPHAM, SLNHAP, SLNTHUC, DVT, CONTAINER_NO, NGAYNHAP, PRICE, TONGTIEN):
        self.MAPN = MAPN
        self.SANPHAM = SANPHAM
        self.SLNHAP = SLNHAP
        self.SLNTHUC = SLNTHUC
        self.DVT = DVT
        self.CONTAINER_NO = CONTAINER_NO
        self.NGAYNHAP = NGAYNHAP
        self.PRICE = PRICE
        self.TONGTIEN = TONGTIEN

class PHIEUXUAT(db.Model):  # Phiếu xuất
    ID_PX = Column(db.Integer, autoincrement=True, primary_key=True)
    MAPX = Column(String(7), nullable=False)
    NGAYDATHANG = Column(String)
    NGAYGIAO = Column(String)
    TENLOAISP = Column(String, nullable=False)
    TENSP = Column(String, nullable=False)
    TRANGTHAI = Column(String)
    SLXUAT = Column(Float)
    SLXTHUC = Column(Float)
    DVT = Column(String(20))  # Thùng hoặc KG
    PRICE = Column(Float)
    TONGTIENPX = Column(String)

    def __init__(self, MAPX, NGAYDATHANG, NGAYGIAO, TENLOAISP,
                 TENSP, TRANGTHAI, SLXUAT, SLXTHUC,  DVT,
                 PRICE, TONGTIENPX):
        self.MAPX = MAPX
        self.NGAYDATHANG = NGAYDATHANG
        self.NGAYGIAO = NGAYGIAO
        self.TENLOAISP = TENLOAISP
        self.TENSP = TENSP
        self.TRANGTHAI = TRANGTHAI
        self.SLXUAT = SLXUAT
        self.SLXTHUC = SLXTHUC
        self.DVT = DVT
        self.PRICE = PRICE
        self.TONGTIENPX = TONGTIENPX

class KHO(db.Model):  # Kho
    ID_KHO = Column(Integer, autoincrement=True, primary_key=True)
    MAKHO = Column(String(10), nullable=False)
    TENKHO = Column(Text, nullable=False)
    TENSP = Column(Text, nullable=False)
    DVT = Column(String(20))
    SLTON = Column(Float)
    DIACHI = Column(Text)
    SDT = Column(String(11))

    def __init__(self, MAKHO, TENKHO, TENSP, DVT, SLTON, DIACHI, SDT):
        self.MAKHO = MAKHO
        self.TENKHO = TENKHO
        self.TENSP = TENSP
        self.DVT = DVT
        self.SLTON = SLTON
        self.DIACHI = DIACHI
        self.SDT = SDT

@app.route('/nhapkho', methods=['GET','POST'])
# @admin_permission.require()
def nhapkho():
    imported_data = 0
    if request.method == 'POST':
        values = request.form['PhieuNhapKho_btn']
        values = values.split("&")

        row_quantity = int(values[1])
        col_quantity = int(values[2])
        table_value = values[3:]

        print(row_quantity)
        print(col_quantity)
        print(table_value)

        rows_value = [table_value[x:x + col_quantity] for x in range(0, row_quantity * col_quantity, col_quantity)]

        for row_value in rows_value:
            print(row_value)

        for row_value in rows_value:
            db.session.add(PHIEUNHAP(row_value[0], row_value[1], float(row_value[2]),
                                     float(row_value[3]), row_value[4], row_value[5],
                                     row_value[6], float(row_value[7]), float(row_value[8])))
        db.session.commit()

        for row_value in rows_value:
            san_pham_trong_kho = KHO.query.filter_by(TENSP=row_value[1]).first()
            if (san_pham_trong_kho != None):
                san_pham_trong_kho.SLTON += float(row_value[2])
                db.session.commit()
            else:
                san_pham_moi = KHO('K01', 'Kho Thủ Đức',row_value[1],
                                         'Kg', row_value[2],'Q.Thủ Đức, Tp.HCM',
                                         '838379828')
                db.session.add(san_pham_moi)
                db.session.commit()
        imported_data = 1
    else:
        # values = request.form['PhieuNhapKho_btn']
        # print(values)
        pass

    return render_template('nhapkho.html', imported_data=imported_data)

@app.route('/xuatkho', methods=['GET','POST'])
# @admin_permission.require()
def xuatkho():
    imported_data = 0
    if request.method == 'POST':
        values = request.form['PhieuXuatKho_btn']
        values = values.split("&")

        row_quantity = int(values[1])
        col_quantity = int(values[2])
        table_value = values[3:]

        print(row_quantity)
        print(col_quantity)
        print(table_value)

        rows_value = [table_value[x:x + col_quantity] for x in range(0, row_quantity * col_quantity, col_quantity)]
        for row_value in rows_value:
            print(row_value)

        for row_value in rows_value:
            db.session.add(PHIEUXUAT(row_value[0], row_value[1], row_value[2],
                                     row_value[3], row_value[4], row_value[5],
                                     float(row_value[6]), float(row_value[7]),row_value[8],
                                     float(row_value[9]), row_value[10]))
        db.session.commit()

        for row_value in rows_value:
            san_pham_trong_kho = KHO.query.filter_by(TENSP=row_value[4]).first()
            if (san_pham_trong_kho != None):
                san_pham_trong_kho.SLTON -= float(row_value[6]) #SLXUAT
                db.session.commit()
            else:
                # render_template(Error.html) : there isn't product on warehouse
                pass

        imported_data = 1
    else:
        # values = request.form['PhieuNhapKho_btn']
        # print(values)
        pass
    return render_template('xuatkho.html', imported_data=imported_data)

@app.route('/report')
def report():
    return send_file('report.pdf',attachment_filename=True)

class XNK(db.Model): #Xuaất nhập khẩu
    ID_XNK = Column(Integer, autoincrement=True, primary_key=True)
    Shipper = Column(String(50))
    Cosignee = Column(String(50))
    ETA = Column(String(50))
    Port_of_Discharge = Column(String(50))
    Invoice = Column(String(50))
    Container_No = Column(String(50))
    Goods = Column(String(50))
    Carton = Column(Integer)
    Price = Column(Float)
    Amount_invoice = Column(Float)
    payment_from_Fruits_and_Greens = Column(Float)
    Date_Payment = Column(String(50))
    Credit_note = Column(String(50))
    Balance = Column(Float)
    NOTE = Column(String(50))
    Load_N0 = Column(String(50))

    def __init__(self,Shipper,Cosignee,ETA,Port_of_Discharge,Invoice,Container_No,Goods,Carton,Price,Amount_invoice,
                 payment_from_Fruits_and_Greens,Date_Payment,Credit_note,Balance,NOTE,Load_N0):
        self.Shipper = Shipper
        self.Cosignee = Cosignee
        self.ETA = ETA
        self.Port_of_Discharge = Port_of_Discharge
        self.Invoice = Invoice
        self.Container_No = Container_No
        self.Goods = Goods
        self.Carton = Carton
        self.Price = Price
        self.Amount_invoice = Amount_invoice
        self.payment_from_Fruits_and_Greens = payment_from_Fruits_and_Greens
        self.Date_Payment = Date_Payment
        self.Credit_note = Credit_note
        self.Balance = Balance
        self.NOTE = NOTE
        self.Load_N0 = Load_N0

@app.route('/nhapchungtu', methods=['GET','POST'])
def xuatnhapkhau():
    imported_data = 0
    if request.method == 'POST':

        xnk = XNK(request.form['shipper'], request.form['cosignee'], request.form['eat'], request.form['portofdischarge'],
                  request.form['invoice'], request.form['containerno'],
                  request.form['goods'], request.form['carton'], request.form['priceusd'], request.form['amountinvoice'],
                  request.form['paymentfromfruitsandgreens'], request.form['datepayment'], request.form['creditnote'],
                  request.form['balance'], request.form['note'],
                  request.form['loadno'])
        print(xnk.Shipper)
        print(xnk.Cosignee)
        print(xnk.ETA)
        print(xnk.Port_of_Discharge)
        print(xnk.Invoice)
        print(xnk.Container_No)
        print(xnk.Goods)
        print(xnk.Carton)
        print(xnk.Price)
        print(xnk.Amount_invoice)
        print(xnk.payment_from_Fruits_and_Greens)
        print(xnk.Date_Payment)
        print(xnk.Credit_note)
        print(xnk.Balance)
        print(xnk.NOTE)
        print(xnk.Load_N0)
        db.session.add(xnk)
        db.session.commit()
        imported_data = 1

    return render_template('nhapchungtu.html', imported_data=imported_data)

@app.route('/xemhangton', methods=['GET', 'POST'])
def xemHangTon():
    TenKho = ""
    TenSp = ""
    DVT = ""
    SLT = ""
    SLT1 = 0
    SLT2 = 0
    if request.method == 'POST':
        TenKho = request.form['Kho']
        TenSp = request.form['TenSP']
        DVT = request.form['DVT']
        SLT = request.form['SLT']
        if (SLT != "Tất cả"):
            if (SLT.find('-') > 0):
                index = SLT.find('-')
                SLT1 = float(SLT[0:index])
                SLT2 = float(SLT[index+1:(len(SLT))])
            else:
                SLT1 = float(SLT[1:(len(SLT))])
                SLT2 = float('inf')

    data = []
    # 0000
    if ((TenKho == "Tất cả") & (TenSp == "") & (DVT == "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.all()
    # 0001
    elif ((TenKho == "Tất cả") & (TenSp == "") & (DVT == "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 0010
    elif ((TenKho == "Tất cả") & (TenSp == "") & (DVT != "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(DVT=DVT).all()
    # 0011
    elif ((TenKho == "Tất cả") & (TenSp == "") & (DVT != "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(DVT=DVT).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 0100
    elif ((TenKho == "Tất cả") & (TenSp != "") & (DVT == "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).all()
    # 0101
    elif ((TenKho == "Tất cả") & (TenSp != "") & (DVT == "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 0110
    elif ((TenKho == "Tất cả") & (TenSp != "") & (DVT != "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(DVT=DVT).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).all()
    # 0111
    elif ((TenKho == "Tất cả") & (TenSp != "") & (DVT != "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(DVT=DVT).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 1000
    elif ((TenKho != "Tất cả") & (TenSp == "") & (DVT == "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho).all()
    # 1001
    elif ((TenKho != "Tất cả") & (TenSp == "") & (DVT == "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 1010
    elif ((TenKho != "Tất cả") & (TenSp == "") & (DVT != "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho, DVT=DVT).all()
    # 1011
    elif ((TenKho != "Tất cả") & (TenSp == "") & (DVT != "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho, DVT=DVT).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 1100
    elif ((TenKho != "Tất cả") & (TenSp != "") & (DVT == "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).all()
    # 1101
    elif ((TenKho != "Tất cả") & (TenSp != "") & (DVT == "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()
    # 1110
    elif ((TenKho != "Tất cả") & (TenSp != "") & (DVT != "Tất cả") & (SLT == "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho, DVT=DVT).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).all()
    # 1111
    elif ((TenKho != "Tất cả") & (TenSp != "") & (DVT != "Tất cả") & (SLT != "Tất cả")):
        data = KHO.query.filter_by(TENKHO=TenKho, DVT=DVT).filter(func.lower(KHO.TENSP).contains(func.lower(TenSp))).filter(KHO.SLTON >= SLT1).filter(KHO.SLTON <= SLT2).all()

    return render_template("XemHangTon.html", data=data)

@app.route('/xemchungtu', methods=['GET', 'POST'])
def xemChungTu():
    Shipper = ""
    Port_of_Discharge = ""
    Invoice = ""
    Container_No = ""
    if request.method == 'POST':
        Shipper = request.form['Shipper']
        Port_of_Discharge = request.form['Port']
        Invoice = request.form['Invoice']
        Container_No = request.form['Container']
    data = []
    #0000
    if ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice == "") & (Container_No == "")):
        data = XNK.query.all()
    #0001
    elif ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice == "")& (Container_No != "")):
        data = XNK.query.filter_by(Container_No=Container_No).all()
    #0010
    elif ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice != "") & (Container_No == "")):
        data = XNK.query.filter_by(Invoice=Invoice).all()
    #0011
    elif ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice != "") & (Container_No != "")):
        data = XNK.query.filter_by(Invoice=Invoice, Container_No=Container_No).all()
    #0100
    elif ((Shipper == "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice == "")& (Container_No == "")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge).all()
    #0101
    elif ((Shipper == "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice == "")& (Container_No != "")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge, Container_No=Container_No).all()
    #0110
    elif ((Shipper == "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice != "")& (Container_No == "")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge, Invoice=Invoice).all()
    #0111
    elif ((Shipper == "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice != "")& (Container_No != "")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge, Invoice=Invoice, Container_No=Container_No).all()
    #1000
    elif ((Shipper != "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice == "")& (Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper).all()
    #1001
    elif ((Shipper != "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice == "")& (Container_No != "")):
        data = XNK.query.filter_by(Shipper=Shipper, Container_No=Container_No).all()
    #1010
    elif ((Shipper != "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice != "")& (Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper, Invoice=Invoice).all()
    #1011
    elif ((Shipper != "Tất cả") & (Port_of_Discharge == "Tất cả") & (Invoice != "")& (Container_No != "")):
        data = XNK.query.filter_by(Shipper=Shipper, Invoice=Invoice, Container_No=Container_No).all()
    #1100
    elif ((Shipper != "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice == "")& (Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge).all()
    #1101
    elif ((Shipper != "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice == "")& (Container_No != "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge, Container_No=Container_No).all()
    #1110
    elif ((Shipper != "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice != "")& (Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge, Invoice=Invoice).all()
    #1111
    elif ((Shipper != "Tất cả") & (Port_of_Discharge != "Tất cả") & (Invoice != "")& (Container_No != "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge, Invoice=Invoice, Container_No=Container_No).all()

    for dt in data:
        if (dt == 'None'):
            dt = ''

    return render_template("XemChungTu.html", data=data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
