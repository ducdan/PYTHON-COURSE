# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Date, Float, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import request


Base = declarative_base()
metadata = Base.metadata


class Kho(Base):
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


class PhieuNhap(Base):
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


class PhieuXuat(Base):
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

@app.route('/',methods=['POST'])
def xuat_xnk():
    xuat = PhieuXuat(request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form['']
        request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''])
    db.session.add(xuat)
    db.session.commit()
def nhap_xnk():
    nhap = PhieuNhap(request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form['']
        request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''],request.form[''])
    db.session.add(nhap)
    db.session.commit()
def filter_macontainer(ma):
    filter = PhieuNhap.query.filter_by(ma=request.form[''])
    return render_template('',ma=filter)
def filter_kho(ten):
    f_kho = Kho.query.filter_by(ten=request.form[''])


