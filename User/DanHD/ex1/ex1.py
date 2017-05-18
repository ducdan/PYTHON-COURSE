from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import  Column, ForeignKey, Integer, String, Text, CHAR, Date, DATE, FLOAT, Float, Numeric
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db=SQLAlchemy(app)

class Kho(db.Model):
    MaKho = db.Column(db.CHAR(7), primary_key=True)
    TenKho = db.Column(db.Text)
    LoaiSP = db.Column(db.Text)
    TenSP = db.Column(db.Text)
    DonViTinh = db.Column(db.CHAR)  # Thùng hoặc KG
    SoLuongTon = db.Column(db.Float)
    SoLuongTonThucTe = db.Column(db.Float)
    DiaChi = db.Column(db.Text)
    SDT = db.Column(db.Numeric)
    NhanVienKho = db.Column(db.Text)
    phieunhap = db.relationship('PhieuNhap', backref='owner', lazy='dynamic')
    phieuxuat = db.relationship('PhieuXuat', backref='owner', lazy='dynamic')

    def __init__(self,MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho):
        self.MaKho=MaKho
        self.TenKho=TenKho
        self.LoaiSP=LoaiSP
        self.TenSP=TenSP
        self.DonViTinh=DonViTinh
        self.SoLuongTon=SoLuongTon
        self.SoLuongTonThucTe=SoLuongTonThucTe
        self.DiaChi=DiaChi
        self.SDT=SDT
        self.NhanVienKho=NhanVienKho

def add_Kho(MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho):
    kho=Kho(MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho)
    db.session.add(kho)
    db.session.commit()

class PhieuNhap(Model):
    MaPN = Column(CHAR(7), primary_key = True)
    NCC = Column(Text(20))
    LoaiSP = Column(Text(20))
    TenSP = Column(Text(20))
    SLNhap = Column(Float)
    SLThucNhap = Column(Float)
    DonViTinh = Column(CHAR(7))#Thùng hoặc KG
    Gia = Column(Numeric)
    TongTien = Column(Numeric)
    NgayNhap = Column(DATE)
    NhanVienNhap = Column(Text)
    NoiNhanHang = Column(Text)
    Container = Column(String(20))
    SoHoaDon = Column(String(10)) #Hóa đơn nhập
    Note = Column(db.Text(100))
    id_Kho = Column(db.CHAR(7), ForeignKey('Kho.MaKho'))

    def __init__(self,MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,id_Kho):
        self.MaPN=MaPN
        self.NCC=NCC
        self.LoaiSP=LoaiSP
        self.TenSP=TenSP
        self.SLNhap=SLNhap
        self.SLThucNhap=SLThucNhap
        self.DonViTinh=DonViTinh
        self.Gia=Gia
        self.TongTien=TongTien
        self.NgayNhap=NgayNhap
        self.NhanVienNhap=NhanVienNhap
        self.NoiNhanHang=NoiNhanHang
        self.Container=Container
        self.SoHoaDon=SoHoaDon
        self.Note=Note
        self.id_Kho=id_Kho

def add_PN(MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,id_Kho):
    PN = PhieuNhap(MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,id_Kho)
    db.session.add(PN)
    db.session.commit()

class PhieuXuat(Model):
    MaPX = Column(CHAR(7), primary_key=True)
    TenKH = Column(Text)
    LoaiSP = Column(Text)
    TenSP = Column(Text)
    SLXuat = Column(Float)
    SLThucXuat = Column(Float)
    DonViTinh = Column(CHAR(7))  # Thùng hoặc KG
    Gia = Column(Numeric)
    TongTien = Column(Numeric)
    NgayXuat = Column(DATE)
    NhanVienGiaoHang = Column(Text)
    PhuongTien = Column(String(20))
    TrangThai = Column(Text)
    SoHoaDon = Column(String(10)) #hóa đơn xuất
    Note = Column(String(100))
    id_Kho = Column(CHAR(7), ForeignKey('Kho.MaKho'))

    def __init__(self, MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,id_Kho):
        self.MaPX = MaPX
        self.TenKH = TenKH
        self.LoaiSP = LoaiSP
        self.TenSP = TenSP
        self.SLXuat = SLXuat
        self.SLThucXuat = SLThucXuat
        self.DonViTinh = DonViTinh
        self.Gia = Gia
        self.TongTien = TongTien
        self.NgayXuat = NgayXuat
        self.NhanVienGiaoHang = NhanVienGiaoHang
        self.PhuongTien = PhuongTien
        self.TrangThai = TrangThai
        self.SoHoaDon = SoHoaDon
        self.Note = Note
        self.id_Kho=id_Kho

def add_PX( MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,id_Kho):
    PX = PhieuXuat( MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,id_Kho)
    db.session.add(PX)
    db.session.commit()

@app.route('/')
def hello_world():
    # print("debug")
    print(db)
    db.create_all()
    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True)

