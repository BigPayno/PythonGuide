"""
Title: 

Version: ListSort
Author: Bear Payne
Date: 2019/11/8 15:55
"""
if __name__ == '__main__':
    list0 = ['zero','one','right']
    print(list0)
    list0.sort()
    print(list0)
    list0.sort(reverse=True)
    print(list0)
    list0.sort(key=len)
    print(list0)
    sorted(list0,reverse=True)
    print(list0)