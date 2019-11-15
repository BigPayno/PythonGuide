"""
Title: PandasConfig

Author: Bear Payne
Date: 2019/11/15 08:41
Description:
    
"""
import pandas as pd
from texttable import Texttable


def display(df):
    tb = Texttable()
    tb.set_cols_align(['l' for _ in range(len(df.columns))])
    tb.set_cols_dtype(['t' for _ in range(len(df.columns))])
    tb.header(df.columns.array)
    tb.add_rows(df.values, header=False)
    tb.set_cols_width([18 for _ in range(len(df.columns))])
    print(tb.draw())


if __name__ == '__main__':
    table = pd.read_csv('d:/aum.csv', encoding='gbk')
    display(table)
