"""
Title: DataFrameDel

Author: Bear Payne
Date: 2019/11/14 10:59
Description:
     DataFrame.drop(labels, axis = 1,  level=None, inplace=False)

    labels：索引，单索引或索引的列表；
    axis：1-删列；
    level：多重索引需要指定；
    inplace：是否本地修改。
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
    # 直接删除一行
    aumCsv2 = aumCsv.copy()
    del aumCsv2[0]
    # del aumCsv.loc['a'],error
    println(aumCsv2)

    # drop
    aumCsv3 = aumCsv.copy()
    aumCsv3.drop(['a'], axis=0, inplace=True)
    println(aumCsv3)
    aumCsv3.drop([0], axis=1, inplace=True)
    println(aumCsv3)

