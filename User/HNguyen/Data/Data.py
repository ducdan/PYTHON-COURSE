from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, ForeignKey, Integer, String, Text, CHAR, DATE, Float, Numeric
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db=SQLAlchemy(app)

class Kho(db.Model):
    MaKho = db.Column(db.CHAR(7), primary_key=True)
    TenKho = db.Column(db.Text)
    LoaiSP = db.Column(db.Text)
    TenSP = db.Column(db.Text)
    DonViTinh = db.Column(db.CHAR(7))  # Thùng hoặc KG
    SoLuongTon = db.Column(db.Float)
    SoLuongTonThucTe = db.Column(db.Float)
    DiaChi = db.Column(db.Text)
    SDT = db.Column(db.Numeric)
    NhanVienKho = db.Column(db.Text)
    phieunhap = db.relationship('PhieuNhap', backref='owner', lazy='dynamic')
    phieuxuat = db.relationship('PhieuXuat', backref='owner', lazy='dynamic')

    def __init__(self,MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho):
        self.MaKho = MaKho
        self.TenKho = TenKho
        self.LoaiSP = LoaiSP
        self.TenSP = TenSP
        self.DonViTinh = DonViTinh
        self.SoLuongTon = SoLuongTon
        self.SoLuongTonThucTe = SoLuongTonThucTe
        self.DiaChi = DiaChi
        self.SDT = SDT
        self.NhanVienKho = NhanVienKho

class PhieuNhap(db.Model):
    MaPN = Column(CHAR(7), primary_key = True)
    NCC = Column(Text)
    LoaiSP = Column(Text)
    TenSP = Column(Text)
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
    Note = Column(Text)
    id_Kho = Column(db.CHAR(7), ForeignKey('kho.MaKho'))

    def __init__(self,MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,kid):
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
        self.id_Kho=kid

class PhieuXuat(db.Model):
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
    id_Kho = Column(CHAR(7), ForeignKey('kho.MaKho'))

    def __init__(self, MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,idk):
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
        self.id_Kho=idk

def add_Kho(MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho):
    kho=Kho(MaKho,TenKho,LoaiSP,TenSP,DonViTinh,SoLuongTon,SoLuongTonThucTe,DiaChi,SDT,NhanVienKho)
    db.session.add(kho)
    db.session.commit()


def add_PN(MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,kid):
    PN = PhieuNhap(MaPN,NCC,LoaiSP,TenSP,SLNhap,SLThucNhap,DonViTinh,Gia,TongTien,NgayNhap,NhanVienNhap,NoiNhanHang,Container,SoHoaDon,Note,kid)
    db.session.add(PN)
    db.session.commit()

def add_PX(MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,idk):
    PX = PhieuXuat(MaPX,TenKH,LoaiSP,TenSP,SLXuat,SLThucXuat,DonViTinh,Gia,TongTien,NgayXuat,NhanVienGiaoHang,PhuongTien,TrangThai,SoHoaDon,Note,idk)
    db.session.add(PX)
    db.session.commit()

@app.route('/')
def hello_world():
    print(db)
    # db.create_all()
    # add_Kho( 'K001', 'Kho Thu Duc', 'Cam', 'Cam navel My size 40', 'Thung', '50', '50', 'So 12 duong 6, P.Linh Chieu, Q.Thu Duc', '0838379828', 'Long' )
    # add_Kho( 'K002', 'Kho Tran Dinh Xu', 'Cherry', 'Cherry Lapin 28-30mm', 'Thung', '100', '100', '137/31 Tran Dinh Xu, P.Nguyen Cu Trinh, Q.1', '0838385916', 'Hung' )
    # add_Kho( 'K003', 'Kho Tan Phu', 'Nho', 'Nho den ngon tay Uc', 'Thung', '80', '80', '39 Le Thuc Hoach, P.Phu Tho Hoa, Q.Tan Phu', '0838383838', 'Duong' )
    # add_Kho( 'K004', 'Kho Thu Duc', 'Tao', 'Tao xanh Phap', 'Thung', '90', '90', 'So 12 duong 6, P.Linh Chieu, Q.Thu Duc', '0838379828', 'Long' )
    # add_Kho( 'K005', 'Kho Tran Dinh Xu', 'Cherry', 'Cherry Staccato 26-28mm', 'Thung', '70', '70', '137/31 Tran Dinh Xu, P.Nguyen Cu Trinh, Q.1', '0838385916', 'Hung' )
    # add_Kho( 'K006', 'Kho Tan Phu', 'Nho', 'Nho den khong hat Nam Phi', 'Thung', '60', '60', '39 Le Thuc Hoach, P.Phu Tho Hoa, Q.Tan Phu', '0838383838', 'Duong' )
    # add_Kho( 'K007', 'Kho Thu Duc', 'Cam', 'Cam Valencia Uc', 'Thung', '110', '110', 'So 12 duong 6, P.Linh Chieu, Q.Thu Duc', '0838379828', 'Chau' )
    # add_Kho( 'K008', 'Kho Tran Dinh Xu', 'Cherry', 'Cherry vang NewZealand', 'Thung', '100', '100', '137/31 Tran Dinh Xu, P.Nguyen Cu Trinh, Q.1', '0838385916', 'Vinh' )
    # add_Kho( 'K009', 'Kho Tan Phu', 'Nho', 'Nho xanh khong hat My', 'Thung', '80', '80', '39 Le Thuc Hoach, P.Phu Tho Hoa, Q.Tan Phu', '0838383838', 'Trung' )
    # add_Kho( 'K010', 'Kho Thu Duc', 'Tao', 'Tao Queen NewZealand', 'Thung', '90', '90', 'So 12 duong 6, P.Linh Chieu, Q.Thu Duc', '0838379828', 'Long' )

    # add_PN( 'N0001', 'Freshmax', 'Cam', 'Cam navel My size 40', '50', '50', 'Thung', '60', '3000', '2017/4/18', 'Minh', 'TP.HCM', 'TCLU 1230412', '477641', 'abc', 'K001' )
    # add_PN( 'N0002', 'Freshmax', 'Cherry', 'Cherry Lapin 28-30mm', '60', '60', 'Thung', '50', '3000', '2017/3/20', 'Dat', 'TP.HCM', 'TCLU 1230413', '477640', 'abc', 'K002' )
    # add_PN( 'N0003', 'ASIA FRESH', 'Nho', 'Nho den ngon tay Uc', '70', '70', 'Thung', '50', '3500', '2017/3/21', 'Trang', 'Ha Noi', 'TCLU 1230414', '477639', 'abc', 'K003' )
    # add_PN( 'N0004', 'L&M', 'Tao', 'Tao xanh Phap', '80', '80', 'Thung', '50', '4000', '2017/3/22', 'Dat', 'TP.HCM', 'TCLU 1230415', '477638', 'abc', 'K004' )
    # add_PN( 'N0005', 'DOMEX', 'Cherry', 'Cherry Staccato 26-28mm', '90', '90', 'Thung', '60', '5400', '2017/3/23', 'Tuan', 'Ha Noi', 'TCLU 1230416', '477637', 'abc', 'K005' )
    # add_PN( 'N0006', 'ASIA FRESH', 'Nho', 'Nho den khong hat Nam Phi', '100', '100', 'Thung', '60', '6000', '2017/3/24', 'Minh', 'TP.HCM', 'TCLU 1230417', '477636', 'abc', 'K006' )
    # add_PN( 'N0007', 'Freshmax', 'Cam', 'Cam Valencia Uc', '110', '110', 'Thung', '40', '4400', '2017/3/25', 'Vu', 'Ha Noi', 'TCLU 1230418', '477635', 'abc', 'K007' )
    # add_PN( 'N0008', 'DOMEX', 'Cherry', 'Cherry vang NewZealand', '120', '120', 'Thung', '60', '7200', '2017/3/26', 'Thanh', 'TP.HCM', 'TCLU 1230419', '477634', 'abc', 'K008' )
    # add_PN( 'N0009', 'L&M', 'Nho', 'Nho xanh khong hat My', '130', '130', 'Thung', '30', '3900', '2017/3/27', 'Minh', 'Ha Noi', 'TCLU 1230420', '477633', 'abc', 'K009' )
    # add_PN( 'N0010', 'DOMEX', 'Tao', 'Tao Queen NewZealand', '140', '140', 'Thung', '50', '7000', '2017/3/28', 'Tien', 'TP.HCM', 'TCLU 1230421', '477632', 'abc', 'K010' )


    # add_PX( 'X0001', 'QUEEN LAND Q2', 'Cherry', 'Cherry Lapin 28-30mm', '70', '70', 'Thung', '80', '5600', '2017/4/18', 'Tra', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K002' )
    # add_PX( 'X0002', 'LOTTE GÒ VẤP', 'Cam', 'Cam navel My size 40', '50', '50', 'Thung', '80', '4000', '2017/4/17', 'Tuan', 'Xe May', 'Da Nhan', '477642', 'xyz', 'K001' )
    # add_PX( 'X0003', 'SIÊU THỊ MY MARKET Q3', 'Nho', 'Nho den ngon tay Uc', '70', '70', 'Thung', '80', '5600', '2017/4/16', 'Tri', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K003' )
    # add_PX( 'X0004', 'SATRA PHẠM HÙNG', 'Tao', 'Tao xanh Phap', '50', '50', 'Thung', '80', '4000', '2017/4/15', 'Tra', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K004' )
    # add_PX( 'X0005', 'VINMART A12 PHAN VĂN TRỊ', 'Cherry', 'Cherry Staccato 26-28mm', '70', '70', 'Thung', '80', '5600', '2017/4/14', 'Tri', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K005' )
    # add_PX( 'X0006', 'SIMPLY MART GÒ VẤP', 'Nho', 'Nho den khong hat Nam Phi', '70', '70', 'Thung', '80', '5600', '2017/4/13', 'Tra', 'Xe May', 'Da Nhan', '477642', 'xyz', 'K006' )
    # add_PX( 'X0007', 'SIMPLY MART QUẬN 7', 'Cam', 'Cam Valencia Uc', '70', '70', 'Thung', '80', '5600', '2017/4/12', 'Tuan', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K007' )
    # add_PX( 'X0008', 'LOTTE MART PICO', 'Cherry', 'Cherry vang NewZealand', '70', '70', 'Thung', '80', '5600', '2017/4/11', 'Toan', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K008' )
    # add_PX( 'X0009', 'LOTTE MART NAM SAI GÒN', 'Nho', 'Nho xanh khong hat My', '70', '70', 'Thung', '80', '5600', '2017/4/10', 'Tien', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K009' )
    # add_PX( 'X0010', 'QUEEN LAND Q2', 'Tao', 'Tao Queen NewZealand', '70', '70', 'Thung', '80', '5600', '2017/4/09', 'Tra', 'Xe Tai', 'Da Nhan', '477642', 'xyz', 'K010' )

    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True)

