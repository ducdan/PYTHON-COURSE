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

# class PHIEUNHAP(db.Model):
#     __tablename__ = 'PHIEUNHAP'
#
#     ID_PN = Column(Integer, primary_key=True)
#     MAPN = Column(String(7), nullable=False, unique=True)
#     SLNHAP = Column(Float(53))
#     SLNTHUC = Column(Float(53))
#     DVT = Column(String(20))
#     CONTAINER_NO = Column(String(20))
#     NGAYNHAP = Column(Date)
#     PRICE = Column(Numeric)
#     TONGTIEN = Column(Numeric)
#     Id_lhn = Column(ForeignKey('LOAIHINHNHAP.ID_LHN'))
#     Id_hd = Column(ForeignKey('HOPDONG.ID_HD'))
#     Id_nv = Column(ForeignKey('NHANVIEN.ID_NV'))
#     Id_spn = Column(ForeignKey('SPN.ID_SPN'))
#
#     HOPDONG = relationship('HOPDONG')
#     LOAIHINHNHAP = relationship('LOAIHINHNHAP')
#     NHANVIEN = relationship('NHANVIEN')
#     SPN = relationship('SPN')
#
#     def __init__(self, id, ma, slnhap, slnthuc, dvt, cont, ngaynhap, gia, tongtien, id_lhn, id_hd, id_nv, id_spn):
#         self.ID_PN = id
#         self.MAPN = ma
#         self.SLNHAP = slnhap
#         self.SLNTHUC = slnthuc
#         self.DVT = dvt
#         self.CONTAINER_NO = cont
#         self.NGAYNHAP = ngaynhap
#         self.PRICE = gia
#         self.TONGTIEN = tongtien
#         self.Id_lhn= id_lhn
#         self.Id_hd = id_hd
#         self.Id_nv = id_nv
#         self.Id_spn = id_spn
#
# class PHIEUXUAT(db.Model):
#     __tablename__ = 'PHIEUXUAT'
#
#     ID_PX = Column(Integer, primary_key=True)
#     MAPX = Column(String(7), nullable=False, unique=True)
#     NGAYDATHANG = Column(Date)
#     NGAYGIAO = Column(Date)
#     PHAN_TRAM_DU_THIEU = Column(Text)
#     TRANGTHAI = Column(Text)
#     POST_OF_DISCHARGE = Column(Text)
#     SLXUAT = Column(Text)
#     SLXTHUC = Column(Text)
#     DVT = Column(String(20))
#     PRICE = Column(Numeric)
#     TONGTIEN = Column(Numeric)
#     Id_nv = Column(ForeignKey('NHANVIEN.ID_NV'))
#     Id_kh = Column(ForeignKey('KHACHHANG.ID_KH'))
#     Id_pt = Column(ForeignKey('PHUONGTIEN.ID_PT'))
#     Id_spx = Column(ForeignKey('SPX.ID_SPX'))
#
#     KHACHHANG = relationship('KHACHHANG')
#     NHANVIEN = relationship('NHANVIEN')
#     PHUONGTIEN = relationship('PHUONGTIEN')
#     SPX = relationship('SPX')
#
#     def __init__(self, id, ma, slnhap, slnthuc, dvt, cont, ngaynhap, gia, tongtien, id_lhn, id_hd, id_nv, id_spn):
#         self.ID_PN = id
#         self.MAPN = ma
#         self.SLNHAP = slnhap
#         self.SLNTHUC = slnthuc
#         self.DVT = dvt
#         self.CONTAINER_NO = cont
#         self.NGAYNHAP = ngaynhap
#         self.PRICE = gia
#         self.TONGTIEN = tongtien
#         self.Id_lhn= id_lhn
#         self.Id_hd = id_hd
#         self.Id_nv = id_nv
#         self.Id_spn = id_spn


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
