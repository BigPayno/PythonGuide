"""
Title: 

Version: String2
Author: Bear Payne
Date: 2019/11/8 15:34
"""
if __name__ == '__main__':
    s = 'hello,payne'
    print(len(s))
    print(s.title())
    print(s.count('l',0,len(s)))
    print(s.find('l'))
    print(s.find('lo'))
    print(s.center(20,'*'))
    print(s.rjust(10,' '))
    print(s.strip('e').strip('h'))
    print(f'[length] of [{s}]:{len(s)}')