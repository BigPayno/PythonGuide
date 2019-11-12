"""
Title: Extend

Author: Bear Payne
Date: 2019/11/11 10:40
Description:
    
"""

class Person(object):
    def __init__(self,name,pwd):
        self._name=name
        self._pwd=pwd
    def print(self):
        print(f'name[{self._name}],password[{self._pwd}]')
class Male(Person):
    def __init__(self,person,sex='male'):
        super().__init__(person._name,person._pwd)
    def print(self):
        print(f'name[{self._name}],password[{self._pwd}],sex[male]')
if __name__ == '__main__':
    person = Person('payne','forever')
    male = Male(person)
    person.print()
    male.print()
    male2 =Male(person,'Male')
    male2.print()