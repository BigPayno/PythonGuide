"""
Title: SQL

Author: Bear Payne
Date: 2019/11/14 14:25
Description:
    limit & distinct & condition
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    table = pd.DataFrame(data=[['male', 'payne'], ['female', 'taylor'], ['male', 'zd'], ['male', 'zy']], columns=['sex', 'name'])
    # select * from table limit 3
    table.head(3)

    # select distinct(table.sex) from table
    # select count(table.sex) from table
    println(table['sex'].unique())
    println(table['sex'].nunique())
    # select * from table where table.sex = 'male'
    println(table[table['sex'] == 'male'])

    table2 = pd.DataFrame(data=[[23], [15], [24], ], columns=['age'])
    table = pd.concat([table, table2], axis=1)
    println(table)
    # select name from table where age>20 and sex='male'
    println(table[(table['age'] > 20) & (table['sex'] == 'male')])

    # select * from table where age is not null/is null
    println(table[table['age'].isna()])
    println(table[table['age'].notna()])

    # delete 空行/空列
    println(table)
    println(table.dropna())
    println(table.dropna(axis=1))