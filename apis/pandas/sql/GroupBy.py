"""
Title: GroupBy

Author: Bear Payne
Date: 2019/11/15 10:14
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
    table = pd.DataFrame(data=[[22, 'male', 'payne'], [23, 'female', 'taylor'], [15, 'male', 'zd'], [11, 'male', 'zy']]
                         ,columns=['age', 'gender', 'name'])

    for group, data in table.groupby('gender'):
        println(group)
        println(data)

    for group, data in table.groupby('gender'):
        println(group)
        println(data[['name', 'age']].sort_values(by=[ 'age'], ascending=[True]).iloc[0])