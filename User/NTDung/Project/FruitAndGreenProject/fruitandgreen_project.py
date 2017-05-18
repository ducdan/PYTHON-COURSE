from flask import Flask,render_template,request,send_file
#from flask_principal import Principal, Permission, RoleNeed
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, DECIMAL, Integer, String, Text, CHAR, DATE, Float, ForeignKey


app = Flask(__name__,static_folder='vendors')
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

# admin_permission = Permission(RoleNeed('admin'))
class XNK(db.Model): #Xuaất nhập khẩu
    ID_XNK = Column(Integer, autoincrement=True, primary_key=True)
    Shipper = Column(Text)
    Cosignee = Column(Text)
    ETA = Column(DATE)
    Port_of_Discharge = Column(Text)
    Invoice = Column(String(10))
    Container_No = Column(Text)
    Goods = Column(Text)
    Carton = Column(Integer)
    Price = Column(DECIMAL)
    Amount_invoice = (DECIMAL)
    payment_from_Fruits_and_Greens = Column(DECIMAL)
    Date_Payment = Column(DATE)
    Credit_note = Column(Text)
    Balance = Column(DECIMAL)
    NOTE = Column(Text)
    Load_N0 = Column(Text)

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

class PHIEUNHAP(db.Model):  # Phiếu nhập
    ID_PN = Column(Integer, autoincrement=True, primary_key=True)
    MAPN = Column(CHAR(7), nullable=False, unique=True)
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
    MAPX = Column(String(7), nullable=False, unique=True)
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

# @login_manager.user_loader
# def load_user(userid):
#     return datastore.find_user(id=userid)

# class LoginForm(Form):
#     email = TextField

@app.route('/')
def hello_world():
    db.create_all()
    return render_template('login.html')


@app.route('/nhapkho', methods=['GET','POST'])
# @admin_permission.require()
def nhapkho():
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
    else:
        # values = request.form['PhieuNhapKho_btn']
        # print(values)
        pass
    return render_template('NhapKho.html')

@app.route('/xuatkho', methods=['GET','POST'])
# @admin_permission.require()
def xuatkho():
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
    else:
        # values = request.form['PhieuNhapKho_btn']
        # print(values)
        pass
    return render_template('XuatKho.html')

@app.route('/xemhangton', methods=['GET', 'POST'])
def xemHangTon():
    TenKho = ""
    TenSp = ""
    if request.method == 'POST':
        TenKho = request.form['Kho']
        TenSp = request.form['TenSP']
    data = []
    if ((TenKho == "Tất cả") & (TenSp == "")):
        data = KHO.query.all()
    elif ((TenKho == "Tất cả")):
        data = KHO.query.filter(KHO.TENSP.ilike(TenSp)).all()
    elif ((TenKho != "Tất cả") & (TenSp == "")):
        data = KHO.query.filter_by(TENKHO=TenKho).all()
    else:
        data = KHO.query.filter_by(TENKHO=TenKho).filter(KHO.TENSP.ilike(TenSp)).all()

    return render_template("XemHangTon.html", data=data, TenKho=TenKho, TenSp=TenSp)

@app.route('/xemchungtu', methods=['GET', 'POST'])
def sxemChungTu():
    Shipper = ""
    Port_of_Discharge = ""
    Container_No = ""
    if request.method == 'POST':
        Shipper = request.form['Shipper']
        Port_of_Discharge = request.form['Port']
        Container_No = request.form['Container']
    data = []
    if ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả") & (Container_No == "")):
        data = XNK.query.all()
        #data = XNK.query.filter_by(Cosignee=Cosignee).all()
    elif ((Shipper == "Tất cả") & (Port_of_Discharge == "Tất cả")):
        data = XNK.query.filter_by(Container_No=Container_No).all()
    elif ((Shipper == "Tất cả") & (Container_No == "")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge).all()
    elif ((Shipper == "Tất cả")):
        data = XNK.query.filter_by(Port_of_Discharge=Port_of_Discharge, Container_No=Container_No).all()
    elif ((Port_of_Discharge == "Tất cả") & (Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper).all()
    elif ((Container_No == "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge).all()
    elif ((Port_of_Discharge == "Tất cả")):
        data = XNK.query.filter_by(Shipper=Shipper, Container_No=Container_No).all()
    elif((Shipper != "Tất cả") & (Port_of_Discharge != "Tất cả") & (Container_No != "")):
        data = XNK.query.filter_by(Shipper=Shipper, Port_of_Discharge=Port_of_Discharge, Container_No=Container_No).all()
    return render_template("XemChungTu.html", data=data, Port_of_Discharge=Port_of_Discharge)

@app.route('/nhapkhau')
def nhapkhau():
    # imported_goods = XNK.query.all()
    # for goods in imported_goods:
    #     print(goods)
    db.create_all()
    xnk = XNK('Domex','F&G','2015-11-25','HCM', '477641', 'TCLU 1230412', 'Apple Granny Smith 100', 855,60,None,
              None,None,None,None,None,None)

    db.session.add(xnk)
    db.session.commit()
    print(xnk)
    return 'Nhap khau'





if __name__ == '__main__':
    app.run(debug=True)
