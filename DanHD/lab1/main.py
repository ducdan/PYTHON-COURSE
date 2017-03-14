import math


a=int(input('Nhap a: '))
b=int(input('Nhap b: '))
c=int(input('Nhap c: '))

delta=b**2 -4*a*c
if delta<0:
    print('pt vo nghiem')
elif delta==0:
    print('pt co nghiem kep: {}'.format(-b*1.0/2*a))
else:
    print('pt co 2 nghiem phan biet')
    print('x1 = {}'.format((-b-math.sqrt(delta))/(2*a*1.0)))
    print('x1 = {}'.format((-b+math.sqrt(delta))/(2*a)))

# a=20
# b=15
# print('so tuoi cua toi la {}, em gai toi dang {} tuoi'.format(a,b))
