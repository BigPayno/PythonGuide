"""
Title: Stream

Author: Bear Payne
Date: 2019/11/11 14:24
Description:
    
"""
from functools import reduce

class Stream(object):
    def __init__(self,stream):
        self._stream = stream
    @staticmethod
    def of(stream):
        return Stream(stream)
    def map(self,mapper):
        self._stream=map(mapper,self._stream)
        return self
    def filter(self,filterFun):
        self._stream=filter(filterFun,self._stream)
        return self
    def collect(self,collector):
        return collector(self._stream)
    def reduce(self,reducer):
        return reduce(reducer,self._stream)

if __name__ == '__main__':
    list1 = [1,3,2,5,7,0]
    set1 = Stream.of(list1).filter(lambda x:x>3).map(lambda x:x*x).collect(set)
    map1 = {_: _-1 for _ in set1}
    print(set1)
    print(map1)