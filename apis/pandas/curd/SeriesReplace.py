"""
Title: SeriesReplace

Author: Bear Payne
Date: 2019/11/13 15:54
Description:
    [replace]
    to_replace：要修改的值，可以为列表
    value：改为的值，可以为列表，与to_repalce要匹配；
    inplace：是否在原地修改；
    [rename]
    index：list or dict，list时必须和已有索引长度相同，dict可以部分修改；
    level：多重索引时，可以指定修改哪一重，从0开始递增；
    inplace：是否原地修改。
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(object):
    println(type(object))


if __name__ == '__main__':
    series = pd.Series(['Payno', 'Lei', 'Python', 'Java'], [x for x in range(4)])
    println(series)

    series[0] = 'I'
    series[1:3] = ['Love', 'Payno']

    # source, result, replace
    series.replace('Java', 'Forever', True)
    println(series)

    # 改索引只能整个改，因为是Immutable类型
    series.index = ['a', 'b', 'c', 'd']
    println(series)
    series.rename(index={'a': 1}, inplace=True)
    println(series)