# Nhap vao 3 so a, b, c la 3 canh cua mot tam giac.
# Xac dinh tam giac tao boi a, b, c la tam giac: can, deu, vuong hay vuong can.

a = float(input("Do dai canh 1 cua tam giac: "))
b = float(input("Do dai canh 2 cua tam giac: "))
c = float(input("Do dai canh 3 cua tam giac: "))

#Kiem tra a, b, c nhap vao co phai la number hay string?

if a <= 0 or b <= 0 or c <= 0:
    print("Gia tri canh tam giac khong phu hop")
elif a >= b + c or b >= a + c or c >= a + b:
    print("a, b, c khong phai la 3 canh cua mot tam giac")
elif a == b:
    if c == a:
        print("Tam giac hien tai la tam giac deu")
    elif c ** 2 == a ** 2 + b ** 2:
        print("Tam giac hien tai la tam giac vuong can")
    else:
        print("Tam giac hien tai la tam giac can")
elif b == c:
    if a == c:
        print("Tam giac hien tai la tam giac deu")
    elif a ** 2 == b ** 2 + c ** 2:
        print("Tam giac hien tai la tam giac vuong can")
    else:
        print("Tam giac hien tai la tam giac can")
elif a == c:
    if b == a:
        print("Tam giac hien tai la tam giac deu")
    elif b ** 2 == a ** 2 + c ** 2:
        print("Tam giac hien tai la tam giac vuong can")
    else:
        print("Tam giac hien tai la tam giac can")
elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
    print("Tam giac hien tai la tam giac vuong")
else:
    print("Tam giac hien tai la tam giac thuong")
