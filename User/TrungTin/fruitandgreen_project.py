from flask import Flask,render_template,request,send_file
from DataModel import KHO
app = Flask(__name__,static_folder='vendors')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/nhapkho')
def nhapkho():
    return render_template('PhieuNhapKho.html')


@app.route('/xemhangton')
def hangton():
    return render_template('XemHangTon.html')




@app.route('/phieunhap',methods=['POST'])
def phieunhap():
    nhap = PHIEUNHAP(requet.form['MaPhieuNhap'], requet.form['SoLuongNhap'], requet.form['SoLuongThucNhap'], requet.form['DonViTinh'],
              requet.form['ContainerNo'], requet.form['NgayNhap'],
              requet.form['Gia'], requet.form['TongTien'], requet.form['IdLoaiHinhNhap'], requet.form['IdHopDong'],
              requet.form['IdNhanVien'], requet.form['IdSanPhamNhap'])
    db.session.add(nhap)
    db.session.commit()
    return render_template('PhieuNhapKho.html')
@app.route('/xuatkho',methods=['POST'])
def xuatkho():
    xuat = PHIEUXUAT(requet.form['MaPhieuXuat'], requet.form['NgayDatHang'], requet.form['NgayGiaoHang'], requet.form['PhanTramDuThieu'],
              requet.form['TrangThai'], requet.form['POD'],
              requet.form['SoLuongXuat'], requet.form['SoLuongThuc'], requet.form['DonViTinh'], requet.form['Gia'],
              requet.form['TongTien'], requet.form['IdNhanVien'],request.form['IdKhachHang'],request.form['IdPhuongTien'],request.form['IdSanPhamXuat'])
    db.session.add(xuat)
    db.session.commit()
    return render_template('PhieuXuatKho.html')
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

    return render_template("XemHangTon.html", data = data)

    def xuatnhapkhau():
        xnk = XNK(requet.form['shipper'], requet.form['cosignee'], requet.form['eat'], requet.form['portofdischarge'],
                  requet.form['invoice'], requet.form['containerNo'],
                  requet.form['goods'], requet.form['carton'], requet.form['price'], requet.form['amountinvoice'],
                  requet.form['paymentfromfruitsanhgreens'], requet.form['datepayment'], requet.form['creditnote'],
                  requet.form['balance'], requet.form['note'],
                  requet.form['loadNO'])
        db.session.add(xnk)
        db.session.commit()
        return render_template('XuatNhapKhau.html')


@app.route('/report')
def report():
    return send_file('report.pdf',attachment_filename=True)


if __name__ == '__main__':
    app.run(debug=True)
