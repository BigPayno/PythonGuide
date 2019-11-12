"""
Title: ObjectAnnotations

Author: Bear Payne
Date: 2019/11/11 09:55
Description:
    
"""
class User(object):
    def __init__(self,name,pwd):
        self._name = name
        self._pwd = pwd
    @property
    def name(self):
        return self._name
    @property
    def pwd(self):
        return self._pwd
    @name.setter
    def name(self,name):
        self._name = name


if __name__ == '__main__':
    payne =User('payne','forever')
    payne.name = 'payno'
    print(payne.name)

