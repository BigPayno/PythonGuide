"""
Title: StrAndDt

Author: Bear Payne
Date: 2019/11/14 16:14
Description:
    
"""
import pandas as pd
import datetime
import time


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    table = pd.DataFrame([['a', '2019 01 12'], ['b', '2010 01 12'], ['1', '2020 03 02']]
                         , columns=['name', 'date_time'])
    table['name_is_digit'] = table['name'].str.isdigit()
    println(table[table['name_is_digit']])

    println(table.dtypes)
    # 强制转型为时间类型
    table['date_time'] = table['date_time'].astype('datetime64[ns]')
    println(table.dtypes)
    # order by date_time
    table.sort_values(by=['date_time'], ascending=[True], inplace=True)
    # stringFormatTime
    table['date_time'] = table['date_time'].dt.strftime('%Y %m %d')
    println(table)