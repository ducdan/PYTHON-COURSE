n = int(input('nhap vao so nam: '))
def function():
    if (n % 4 == 0) or (n % 4 == 0 and n % 100 != 0):
        return True
    else:
        return False
print(function())

# a = int(input('nhap vao gia tri a: '))
# n = int(input('nhap vao gia tri n: '))
# def inc():
#     if(n==100):
#         return a+n
#     else:
#         return a+2
#
# print(inc())


# def inc(b,*lst):
#     result=0
#     for x in lst:
#         result+=x
#     return result+b
# a=12
# n=90
# b=0
# b=inc(a,3,4,5)
# print(b)
#


