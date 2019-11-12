"""
Title: 

Version: Collection
Author: Bear Payne
Date: 2019/11/8 15:41
"""
if __name__ == '__main__':
    list1 = ['a','b',1]
    list1.append('abc')
    list1 += [1,2,3]
    list1.insert(1,'zero')
    for x in list1:
        print(x)
        print(type(x))
    if 1 in list1:
        list1.remove(1)
    list1.pop(0)
    for x in list1[0:3]:
        print(x)
    print(list1[:])
    print(list1[0:-1])
    print(list1[-3:])
    list1.clear()

