"""
Title: StaticClassMethod

Author: Bear Payne
Date: 2019/11/11 10:04
Description:
    
"""
from time import time,localtime,sleep

class Clock(object):
    def __init__(self,second=0,min=0,hour=0):
        self._hour = hour
        self._min = min
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return Clock(ctime.tm_sec,ctime.tm_min,ctime.tm_hour)
    @staticmethod
    def of(hour,min,sec):
        return Clock(hour,min,sec)
    def to_str(self):
        return f'hour[{self._hour}],min[{self._min}],sec[{self._second}]';
if __name__ == '__main__':
    clock = Clock.now()
    print(clock.to_str())
    clock2 = Clock.of(2,2,2)
    print(clock2.to_str())