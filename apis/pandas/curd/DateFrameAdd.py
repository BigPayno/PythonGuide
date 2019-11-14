"""
Title: DateFrameAdd

Author: Bear Payne
Date: 2019/11/14 10:47
Description:
     pd.concat(objs, axis=0)
    确保 列索引 相同，行增加。 （其实这个函数并不要求列索引相同，它可以选择出相同的列。而我写这个教程遵循了python的宣言—明确：做好一件事有一种最好的方法，精确控制每一步，可以少犯错。）
    objs: list of DataFrame；
    axis: 取0，进行行增加操作。

"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    aumCsv = pd.DataFrame(data=[['male', 'payne'], ['female', 'taylor']], index=['a', 'b'])
    # 直接增一行
    aumCsv.loc['c'] = ['male', 'zl']
    println(aumCsv)

    # 函数增多行
    aumCsv2 = pd.DataFrame(data=[['male', 'payne'], ['female', 'taylor']], index=['c', 'd'])
    println(pd.concat([aumCsv, aumCsv2], axis=0))

    # 直接增一列
    aumCsv['age'] = ['25', '26', '27']
    println(aumCsv)

    # 函数增多列 axis代表增加的维度，0是行，1是列
    aumCsv3 = pd.DataFrame(data=[[25], [26], [27]], index=['a', 'b', 'c'], columns=['age2'])
    println(pd.concat([aumCsv,aumCsv3], axis=1))