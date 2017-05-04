from flask import Flask,render_template,request,send_file
from DataModel import KHO
from DataModel import PHIEUNHAP,PHIEUXUAT,XNK
app = Flask(__name__,static_folder='vendors')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/nhapkho')
def nhapkho():
    return render_template('PhieuNhapKho.html')

@app.route('/xuatkho')
def xuatkho():
    return render_template('PhieuXuatKho.html')

@app.route('/xnk')
def xnk():
    return render_template('XuatNhapKhau.html')


@app.route('/xemhangton')
def hangton():
    return render_template('XemHangTon.html')




@app.route('/phieunhap',methods=['POST'])
def phieunhap():
    if request.method == 'POST':

        nhap = PHIEUNHAP(MAPN=request.form['MaPhieuNhap'],SLNHAP=request.form['SoLuongNhap'], SLNTHUC=request.form['SoLuongThucNhap'], DVT=request.form['DonViTinh'],
              CONTAINER_NO=request.form['ContainerNo'], NGAYNHAP=request.form['NgayNhap'],
              PRICE=request.form['Gia'], TONGTIEN=request.form['TongTien'], idlhn=request.form['IdLoaiHinhNhap'], idhd=request.form['IdHopDong'],
              idnv=request.form['IdNhanVien'], idspn=request.form['IdSanPhamNhap'])
    db.session.add(nhap)
    db.session.commit()
    return render_template('PhieuNhapKho.html')
@app.route('/phieuxuat',methods=['POST'])
def phieuxuat():
    if request.method == 'POST':

        xuat = PHIEUXUAT(MAPX=request.form['MaPhieuXuat'], NGAYDATHANG=request.form['NgayDatHang'], NGAYGIAO=request.form['NgayGiaoHang'], PHANTRAMDUTHIEU=request.form['PhanTramDuThieu'],
              TRANGTHAI=request.form['TrangThai'], POST_OF_DISCHARGE=request.form['POD'],
              SLXUAT=request.form['SoLuongXuat'], SLXTHUC=request.form['SoLuongThuc'], DVT=request.form['DonViTinh'], PRICE=request.form['Gia'],
              TONGTIEN=request.form['TongTien'], idnv=request.form['IdNhanVien'],idkh=request.form['IdKhachHang'],idpt=request.form['IdPhuongTien'],idspx=request.form['IdSanPhamXuat'])
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
app.route('/xuatnhatkhau', method=['POST'])
def xuatnhapkhau():
    if request.method == 'POST':
        xnk = XNK(request.form['shipper'], request.form['cosignee'], request.form['eat'], request.form['portofdischarge'],
                  request.form['invoice'], request.form['containerNo'],
                  request.form['goods'], request.form['carton'], request.form['price'], request.form['amountinvoice'],
                  request.form['paymentfromfruitsanhgreens'], request.form['datepayment'], request.form['creditnote'],
                  request.form['balance'], request.form['note'],
                  request.form['loadNO'])
        db.session.add(xnk)
        db.session.commit()
        return render_template('XuatNhapKhau.html')

#@app.route('/admin')
    #username=request.form['admin']
   # user=User()
   # rs=user.query.filter_by(username=username).first()
    #rs=['role']!='admin'
@app.route('/report')
def report():
    return send_file('report.pdf',attachment_filename=True)


if __name__ == '__main__':
    app.run(debug=True)
