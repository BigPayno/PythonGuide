"""
Title: 

Version: Fun
Author: Bear Payne
Date: 2019/11/8 15:09
"""

def cusSum(a,b):
    return a+b
def cusSum2(*args):
    result = 0.0
    for x in args:
        result += x
    return result


if __name__ == '__main__':
    print(cusSum(5,5.2))
    print(cusSum2(1,2,3,4,5))

