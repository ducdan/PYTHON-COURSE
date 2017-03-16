a = int(input('Nhap canh a: '))
b = int(input('Nhap canh b: '))
c = int(input('Nhap canh c: '))

if(a <= 0 or b <= 0 or c <= 0):
    print('Moi ban nhap lai!')
elif(a==b):
    if(a==c):
        print('Day la tam giac deu')
    else:
        print('Day la tam giac can')
elif(a==c):
    if(a==b):
        print('Day la tam giac deu')
    else:
        print('Day la tam giac can')
elif(b==c):
    if(b==a):
        print('Day la tam giac deu')
    else:
        print('Day la tam giac can')
elif(a**2==b**2 + c**2):
    if(b==c):
        print('Day la tam giac vuong can')
    else:
        print('Day la tam giac vuong')
elif(b**2==a**2 + c**2):
    if(a==c):
        print('Day la tam giac vuong can')
    else:
        print('Day la tam giac vuong')
elif(c**2==a**2 + b**2):
    if(a==b):
        print('Day la tam giac vuong can')
    else:
        print('Day la tam giac vuong')
else:
    print('Day la tam giac thuong')
