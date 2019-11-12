"""
Title: Tuple

Author: Bear Payne
Date: 2019/11/11 09:02
Description:
    List: mutable,LinkedList
    Tuple : Immutable,?List
"""
if __name__ == '__main__':
    tuple = ('a',5,1.2)
    print(tuple)
    print(tuple[:-1])
    # 变量tuple重新引用了新的元组原来的元组将被垃圾回收
    tuple = ('王大锤', 20, True, '云南昆明')
    list = list(tuple)
    print(list)
    tuple = tuple(list)