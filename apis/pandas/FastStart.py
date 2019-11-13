"""
Title: FastStart

Author: Bear Payne
Date: 2019/11/12 14:43
Description:
    pandas quick start
"""
import pandas as pd
import numpy as np
import codecs


if __name__ == '__main__':
    aumCsv = pd.read_csv('d:/aum.csv',sep=',',encoding='gbk')
    print(f'csv columns[{aumCsv.shape[0]}],rows[{aumCsv.shape[1]}]')
    print(f'{aumCsv.head(2)}')
    print(aumCsv.info())
    print(aumCsv.index)
    print(aumCsv.groupby('性别代码'))