"""
Title: 

Version: IfElse
Author: Bear Payne
Date: 2019/11/8 15:00
"""
a = int(input('please write a num in scanner!'))
if(a == 0):
    print('your input is 0')
else:
    print('your input is not 0')
b = float(input('please input x'))
if b < 0:
    print(b)
elif b == 0:
    print(10)
else:
    print(b * b)
