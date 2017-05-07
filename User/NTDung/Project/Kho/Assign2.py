from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, Numeric, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
db = SQLAlchemy(app)

class KHO(db.Model):
    __tablename__ = 'KHO'

    ID_KHO = Column(Integer, primary_key=True)
    MAKHO = Column(String(10), nullable=False, unique=True)
    TENKHO = Column(Text, nullable=False, unique=True)
    DIACHI = Column(Text)
    SDT = Column(String(11))
    Id_pn = Column(ForeignKey('PHIEUNHAP.ID_PN'))
    Id_px = Column(ForeignKey('PHIEUXUAT.ID_PX'))

    #PHIEUNHAP = relationship('PHIEUNHAP')
    #PHIEUXUAT = relationship('PHIEUXUAT')

    def __init__(self, id, makho, tenkho, diachi, sdt):
        self.ID_KHO = id
        self.MAKHO = makho
        self.TENKHO = tenkho
        self.DIACHI = diachi
        self.SDT = sdt


@app.route('/xemkho', methods=['GET', 'POST'])
def show_kho():
    kho = ""
    MaKho = ""
    LoaiSp = ""
    TenSp = ""
    if request.method == 'POST':
        kho = request.form['Kho']
        MaKho = kho[0:4]
        LoaiSp = request.form['LoaiSP']
        TenSp = request.form['TenSP']
    data = []
    if ((kho == "Tất cả") & (LoaiSp == "") & (TenSp == "")):
        data = KHO.query.all()
    elif ((kho == "Tất cả") & (LoaiSp == "")):
        pass
    elif ((kho == "Tất cả") & (TenSp == "")):
        pass
    elif ((kho == "Tất cả")):
        pass
    elif ((LoaiSp == "") & (TenSp == "")):
        data = KHO.query.filter_by(MAKHO=MaKho).all()
    elif ((TenSp == "")):
        pass
    elif ((LoaiSp == "")):
        pass
    else:
        pass

    return render_template("Hangton.html", data = data)


if __name__ == '__main__':
    app.run(debug=True)
