"""
Title: Filter

Author: Bear Payne
Date: 2019/11/11 11:04
Description:
    
"""

if __name__ == '__main__':
    list1 = [x for x in range(10)]
    list2 = list(filter(lambda x:x>5,list1))
    print(list2)

    list1 = [2,5,3,7,1,1]