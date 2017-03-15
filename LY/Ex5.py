# Kiem tra mot nam co phai la nam nhuan hay khong

# Xac dinh gia tri nhap vao co phu hop hay khong?
while True:
    try:
        year = int(input("Nam can xac dinh: "))
    except ValueError:
        print("Xin nhap lai: ")
        continue
    else:
        break

if 0 < year < 9999:
    if year % 400 == 0:
        print("Nam do la nam nhuan")
    else:
        print("Nam do khong phai la nam nhuan")
else:
    print("Nam ban muon xac dinh khong hop ly")