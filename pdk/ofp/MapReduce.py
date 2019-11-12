"""
Title: Map

Author: Bear Payne
Date: 2019/11/11 11:03
Description:
    
"""
from functools import reduce


def printt(var):
    print(f'var:[{var}],type[{type(var)}]')

if __name__ == '__main__':
    list1 = [x for x in range(1,10)]
    fun = lambda x : x*x
    printt(fun)
    printt(map(fun,list1))
    printt(list(map(fun,list1)))

    printt(reduce(lambda x,y:max(x,y),list1))
    printt(int(reduce(lambda x,y:max(x,y),list1)))