"""
Title: DataFrameQuery

Author: Bear Payne
Date: 2019/11/13 15:22
Description:
    
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    aumCsv = pd.read_csv('d:/aum.csv',encoding='gbk')
    println(aumCsv)
    # [], 快速查询,基于行
    println(aumCsv[:])
    println(aumCsv[[False,True]])
    # [], 快速查询,基于列
    println(aumCsv['客户编号'])
    println(aumCsv[['客户编号', '客户名称']])
    # loc[]，基于索引
    println(aumCsv.loc[0, ['客户编号', '客户名称']])

    # .iloc[]，基于位置 [行，列] [:] (前闭后开)
    println(aumCsv.iloc[1, 1])
    println(aumCsv.iloc[0, 1])
    println(aumCsv.iloc[0, 2])
    println(aumCsv.iloc[0:2, 1])
    println(aumCsv.iloc[0:2, 0:5])
