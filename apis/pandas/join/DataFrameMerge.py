"""
Title: DataFrameMerge

Author: Bear Payne
Date: 2019/11/14 11:08
Description:

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort = False)

concat函数本质上是在所有索引上同时进行对齐合并，而如果想在任意列上对齐合并，则需要merge函数，其在sql应用很多。

    left,right： 两个要对齐合并的DataFrame；
    how： 先做笛卡尔积操作，然后按照要求，保留需要的，缺失的数据填充NaN；
        left: 以左DataFrame为基准，即左侧DataFrame的数据全部保留（不代表完全一致、可能会存在复制），保持原序
        right: 以右DataFrame为基准，保持原序
        inner: 交，保留左右DataFrame在on上完全一致的行，保持左DataFrame顺序
        outer: 并，按照字典顺序重新排序
    on：列索引或列索引列表，如果要在DataFrame相同的列索引做对齐，用这个参数；
    left_on, right_on, left_index, right_index：
        on对应普通的列索引或列索引列表，对齐不同列名的DataFrame，用这俩参数；
        index对应要使用的index，建议不要使用这俩参数，因为可以用concat方法代替。
    sort: True or False，是否按字典序重新排序。
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    gender_name = pd.DataFrame(data=[['male', 'payne'], ['female', 'taylor']], columns=['sex', 'name'], index=['a', 'b'])
    id_name = pd.DataFrame(data=[['001', 'payne'], ['002', 'taylor'], ['003', 'zed']], columns=['id', 'name'], index=['0', '1', '2'])

    # 数据库内连接查询
    table1 = pd.merge(gender_name, id_name, how='inner', on=['name'])
    println(table1)

    # 数据库左连接查询
    table2 = pd.merge(id_name, gender_name, how='left',on=['name'])
    println(table2)

    # select 'id','sex','name','age'
    #      from id_gender_name as a left_join id_sid_age as b
    #      on a.id=b.sid
    id_gender_name = pd.DataFrame(data=[['001', 'male', 'payne'], ['002', 'female', 'taylor']], columns=['id', 'sex', 'name'])
    id_sid_age = pd.DataFrame(data=[['001', '001', 25], ['003', '002', 27]], columns=['id', 'sid', 'age'])
    table3 = pd.merge(id_gender_name, id_sid_age[['sid', 'age']], how='inner', left_on=['id'], right_on=['sid'])
    println(table3[['id', 'sex', 'name', 'age']])



