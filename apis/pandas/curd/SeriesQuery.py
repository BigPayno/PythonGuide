"""
Title: Curd

Author: Bear Payne
Date: 2019/11/12 17:00
Description:
    
"""
import pandas as pd
import numpy as np


def println(word):
    print(word)
    print()


if __name__ == '__main__':
    # [], 快速查询
    aumCsv = pd.read_csv('d:/aum.csv',encoding='gbk')
    series = aumCsv['客户名称']
    println(series[0])
    println(series[:1])
    println(series[[0, 1]])
    println(series[[False,True]])

    # loc[]，基于索引
    series = pd.Series([1, 2], ['a', 'b'])
    println(series)
    println(series.loc['a'])
    println(series.loc['a':'b'])
    println(series.loc[[False,False]])

    # .iloc[]，基于位置
    println(series.iloc[0:2])
