"""
Title: SetOpts

Author: Bear Payne
Date: 2019/11/11 09:19
Description:
    
"""
if __name__ == '__main__':
    setA = {0,1,3,5,7,9}
    setB = {2,4,6,8,0}
    setC = {2,4}
    # 集合的交集、并集、差集、对称差运算
    print(setA & setB)
    # print(set1.intersection(set2))
    print(setA | setB)
    # print(set1.union(set2))
    print(setA - setB)
    # print(set1.difference(set2))
    print(setA ^ setB)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(setC <= setB)
    # print(set2.issubset(set1))
