from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Date, Float, ForeignKey, Numeric, String, Text, text

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
db = SQLAlchemy(app)

class Kho(db.Model):
    __tablename__ = 'kho'

    MaKho = Column(String(7), primary_key=True)
    TenKho = Column(Text)
    LoaiSP = Column(Text)
    TenSP = Column(Text)
    DonViTinh = Column(String(7))
    SoLuongTon = Column(Float(53))
    SoLuongTonThucTe = Column(Float(53))
    DiaChi = Column(Text)
    SDT = Column(Numeric)
    NhanVienKho = Column(Text)

    def __init__(self, MaKho, TenKho, DiaChi, SDT, NVKho):
        self.MaKho = MaKho
        self.TenKho = TenKho
        self.DiaChi = DiaChi
        self.SDT = SDT
        self.NhanVienKho = NVKho

class PhieuNhap(db.Model):
    __tablename__ = 'phieu_nhap'

    MaPN = Column(String(7), primary_key=True)
    NCC = Column(Text)
    LoaiSP = Column(Text)
    TenSP = Column(Text)
    SLNhap = Column(Float(53))
    SLThucNhap = Column(Float(53))
    DonViTinh = Column(String(7))
    Gia = Column(Numeric)
    TongTien = Column(Numeric)
    NgayNhap = Column(Date)
    NhanVienNhap = Column(Text)
    NoiNhanHang = Column(Text)
    Container = Column(String(20))
    SoHoaDon = Column(String(10))
    Note = Column(Text)
    id_Kho = Column(ForeignKey('kho.MaKho'))

    kho = relationship('Kho')

    def __init__(self, MaPN, NCC, Container, SoHD, Kho):
        self.MaPN= MaPN
        self.NCC= NCC
        self.Container = Container
        self.SoHoaDon = SoHD
        self.id_Kho = Kho


class PhieuXuat(db.Model):
    __tablename__ = 'phieu_xuat'

    MaPX = Column(String(7), primary_key=True)
    TenKH = Column(Text)
    LoaiSP = Column(Text)
    TenSP = Column(Text)
    SLXuat = Column(Float(53))
    SLThucXuat = Column(Float(53))
    DonViTinh = Column(String(7))
    Gia = Column(Numeric)
    TongTien = Column(Numeric)
    NgayXuat = Column(Date)
    NhanVienGiaoHang = Column(Text)
    PhuongTien = Column(String(20))
    TrangThai = Column(Text)
    SoHoaDon = Column(String(10))
    Note = Column(String(100))
    id_Kho = Column(ForeignKey('kho.MaKho'))

    kho = relationship('Kho')

    def __init__(self, MaPX, TenKH, SoHD, Kho):
        self.MaPX= MaPX
        self.TenKH= TenKH
        self.SoHoaDon = SoHD
        self.id_Kho = Kho


@app.route('/kho')
def show_kho():
    kho = Kho.query.all()
    return render_template("Kho.html", kho=kho)

@app.route('/nhap')
def show_nhap():
    nhap = PhieuNhap.query.all()
    return render_template("PhieuNhap.html", nhap=nhap)

@app.route('/xuat')
def show_xuat():
    xuat = PhieuXuat.query.all()
    return render_template("PhieuXuat.html", xuat=xuat)




if __name__ == '__main__':
    app.run(debug=True)
