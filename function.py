# function in python


def add(a = 6 ,*args,**kwargs):
    sum = 0
    for a in args:
        sum += a
    return  sum   

print(add(1,2,3,4,5,7))
print(add(1,2,3,4,5,7,6,7,8,9,9,0))



# a_set = set()
# names = ['Munya']
# unique_names = set(names)
# for name in unique_names:
#     print(name)
# unique_names





#
# def add(a = 0,b = 0,**kwargs):
#     return  a + b
# def sub(a,b):
#     return  a - b
#
# def mul(a,b):
#     return  a * b
#
# print(add())
#
# def scan_function(target='127.0.0.0'):
#     print(target)
#
# print(scan_function())
# print(scan_function('192.168.1.166'))
# print(add())
#
# print(add(12,45))
# # print(mul(12888,45))
# # print(sub(12888,45))