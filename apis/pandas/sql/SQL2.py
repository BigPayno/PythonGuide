"""
Title: SQL2

Author: Bear Payne
Date: 2019/11/14 14:50
Description:
    group by & count & sum/max/min & union & order by & case when
"""
import pandas as pd
import numpy as np


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


def age_range(age):
    if age<18:
        return '青年'
    elif 18<=age<36:
        return '中年'
    else:
        return 'unknown'


if __name__ == '__main__':
    table = pd.DataFrame(data=[[22, 'male', 'payne'], [23, 'female', 'taylor'], [15, 'male', 'zd'], [11, 'male', 'zy']], columns=['age', 'gender', 'name'])

    # select gender, count({distinct} age) from table group by gender
    println(table.groupby('gender')['age'].nunique())
    println(table.groupby('gender')['age'].size())
    println(table.groupby('gender')['age'].count())

    # select gender, count(distinct name), sum(age) from table group by gender
    println(table.groupby('gender').agg({'name': np.size, 'age': np.sum}))

    # select gender, count(distinct name) as name_count, sum(age) as age_sun from table group by gender
    println(table.groupby('gender').agg({'name': np.size, 'age': np.sum}).rename(columns={'name': 'name_count','age': 'age_sum'}))

    table2 = pd.DataFrame(data=[[22, 'male', 'payne'], [23, 'female', 'ketty']], columns=['age', 'gender', 'name'])
    # select * from table union select * from table2
    println(pd.concat([table,table2]).drop_duplicates())

    # select * from table order by gender desc, age
    println(table.sort_values(by=['gender', 'age'],ascending=[False, True]))

    table['age_range'] = table['age'].map(age_range)
    println(table)