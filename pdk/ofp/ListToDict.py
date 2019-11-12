"""
Title: ListToDict

Author: Bear Payne
Date: 2019/11/11 14:47
Description:
    
"""
class Person(object):
    def __init__(self,name,pwd):
        self._name=name
        self._pwd=pwd
    @property
    def name(self):
        return self._name
    @name.setter
    def set_name(self,namr):
        self._name=namr

if __name__ == '__main__':
    payno =Person('payno','2345')
    bear =Person('bear','138')
    map = {person.name:person for person in [payno,bear]}
    for key in map:
        if(isinstance(map.get(key),Person)):
            print(f'{key}:{map.get(key)._pwd}')