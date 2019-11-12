"""
Title: Dict

Author: Bear Payne
Date: 2019/11/11 09:21
Description:
    
"""
if __name__ == '__main__':
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)
    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    print(items1)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    print(items2)
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items3)
    items4 = {num: chr(num) for num in range(1,20)}
    print(items4)
    items5 = {'a':items1,'b':'a'}
    items5.update(冷面=67, 方启鹤=85)
    for key in items5:
        print(f'{key}:{items5[key]}')
    print(items5.get('b'))
    print(items5.get('c',6))
    print(items5.popitem())
    print(items5.pop('b'))
    if 'b' not in items5.keys():
        print('b has been removed')
    items5.clear()
