"""
Title: Set

Author: Bear Payne
Date: 2019/11/11 09:06
Description:
    
"""
if __name__ == '__main__':
    setA = {0,1,3,5,7,9}
    setB = {0,2,4,6,8,10}
    setC = {range(5,11)}
    setD = {var for var in range(1,11) if var % 2 == 0 and var >5}
    print(setD)

    setA.add(11)
    if 11 in setA:
        setA.remove(11)
    # discard => removeIfExist
    setA.discard(11)
    setA.update([10,11])
    print(setA)
    for _ in range(1,len(setA)):
        print(setA.pop())


