"""
Title: Lists

Author: Bear Payne
Date: 2019/11/11 09:33
Description:
    
"""

def max(list):
    max = list[0]
    for index in range(0,len(list)-1):
        if(list[index]>max):
            max = list[index]
    return max

if __name__ == '__main__':
    list = [1,6,7,4,0]
    print(max(list))