"""
Title: String3

Author: Bear Payne
Date: 2019/11/11 16:10
Description:
    list[],set、map{},tuple()
"""
if __name__ == '__main__':
    # 字符串转换成列表
    a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
    print(type(a))
    b = eval(a)
    print(type(b))
    print(b)
    print(b[0])
    print(type(b[0]))

    # 字符串转换成字典
    a = "{1: 'a', 2: 'b'}"
    print(type(a))
    b = eval(a)
    print(type(b))
    print(b)

    # 字符串转换成元组
    a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
    print(type(a))
    b = eval(a)
    print(type(b))
    print(b)

