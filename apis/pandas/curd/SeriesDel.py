"""
Title: SeriesDel

Author: Bear Payne
Date: 2019/11/13 16:25
Description:
     Series.drop(labels, level=None, inplace=False)
    labels：索引，单索引或索引的列表；
    level：多重索引需要设置；
    inplace：是否本地修改。

"""
import pandas as pd

if __name__ == '__main__':
    series = pd.Series(['a', 'b', 1, 'd'], range(4))
    print(series)
    del series[1]
    print(series)
    series.drop([2, 3], inplace=True)
    print(series)