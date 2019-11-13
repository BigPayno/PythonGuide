"""
Title: SeriesAdd

Author: Bear Payne
Date: 2019/11/13 16:14
Description:
     Series.append(to_append, ignore_index=False, verify_integrity=False)
    to_append: 另一个series或多个Series构成的列表；
    ignore_index：False-保留原有索引，True-清除所有索引，生成默认数值索引；
    verify_integrity：True的情况下，如果to_append索引与当前索引有重复，则报错。

"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(object):
    println(type(object))


if __name__ == '__main__':
    series = pd.Series(['i', 'l', 'p', 'f'], range(4))

    # 直接在查基础上
    series[4] = '!'
    series.loc[5] = '!'
    println(series)

    # 函数
    appendSeries = pd.Series(['a', 'b'], range(5, 7))
    series =series.append(to_append=appendSeries, ignore_index=True)
    println(series)