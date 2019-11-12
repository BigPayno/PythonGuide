"""
Title:
    int()：将一个数值或字符串转换成整数，可以指定进制。
    float()：将一个字符串转换成浮点数。
    str()：将指定的对象转换成字符串形式，可以指定编码。
    chr()：将整数转换成该编码对应的字符串（一个字符）。
    ord()：将字符串（一个字符）转换成对应的编码（整数）。
Version: VarTo
Author: Bear Payne
Date: 2019/11/8 14:43
"""
a = 331.5
print(float(a))
print(type(float(a)))
print(str(a))
print(type(str(a)))
print(chr(int(a/10)))
print(ord('c'))