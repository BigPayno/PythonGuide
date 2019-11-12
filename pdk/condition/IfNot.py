"""
Title: IfNot

Author: Bear Payne
Date: 2019/11/11 11:04
Description:
    None,False,0,空列表[],空字典{},空元祖(),都相当于false
"""
class Objs(object):
    @staticmethod
    def is_valid_data(data):
        if data == 0:
            return False
        if not not data:
            return False
        return True
if __name__ == '__main__':
    print(Objs.is_valid_data(0))
    print(Objs.is_valid_data([]))