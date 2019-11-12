"""
Title: Object

Author: Bear Payne
Date: 2019/11/11 09:49
Description:
    
"""
class User(object):
    def __init__(self,name,pwd,__secret):
        self.name = name
        self.pwd = pwd
        self.__secret = 'secret'
    def print(self):
        print(f'name:[{self.name}],password:[{self.pwd}]')

if __name__ == '__main__':
    user = User('payno','forever')
    user.print()
    print(user.name)