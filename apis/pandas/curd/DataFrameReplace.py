"""
Title: DataFrameReplace

Author: Bear Payne
Date: 2019/11/14 10:33
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
    # .loc[]方法确保在原地修改
    aumCsv.loc[0, '客户名称'] = 'zd'
    println(aumCsv.loc[0, '客户名称'])

    # DataFrame.replace(to_replace=None, value=None, inplace=False)
    aumCsv.replace('zd','zd2',True)
    println(aumCsv.loc[0, '客户名称'])

    # 交换两列内容
    aumCsv[['客户名称', '客户编号']] = aumCsv[['客户编号', '客户名称']]
    println(aumCsv)

    # 改变某一列
    aumCsv['客户编号'] = pd.Series(['a','b'])
    println(aumCsv)

    # 索引类似于tuple，必须全改，不能切片修改
    aumCsv.index = aumCsv['客户身份证']
    println(aumCsv)

    # DataFrame.rename(index=None, columns = None,  level = None, inplace = False),可以用dict进行部分修改
    aumCsv.rename({'32072119951220023X': '001'}, inplace=True)
    println(aumCsv)
