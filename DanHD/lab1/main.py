import random


lst=[3,4,5,67,8,9]
for x in lst:
    print(x)

john={
    'family_name':'Nguyen',
    'birthday':'19/2',
    'gender':'male'
}
john['gender']='female'
print(john)
john.pop('gender')
print(john)
print(john.get('gender'))
for key in john:
    print(key)
for key in john.keys():
    print(key)
    print(john[key])




def count(a,lst=[3,4,5]):
    result=0
    for x in lst:
        result+=x
    return a+result