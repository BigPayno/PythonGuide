"""
Title: SeriesAndDataFrame

Author: Bear Payne
Date: 2019/11/12 16:13
Description:

1.2.1 data无索引
    如果 data 为 ndarray(1D) 或 list(1D)，那么其缺少 Series 需要的索引信息；
    如果提供 index，则必须和data长度相同；
    如果不提供 index，那么其将生成默认数值索引 range(0, data.shape[0])。
1.2.2 data有索引
    如果 data 为 Series 或 dict ，那么其已经提供了 Series 需要的索引信息，所以 index 项是不需要提供的；
    如果额外提供了 index 项，那么其将对当前构建的Series进行 重索引（增删）（等同于reindex操作）。
2.1 data无 行索引，无 列索引
    如果 data 为 ndarray(2D) or list(2D)，那么其缺少 DataFrame 需要的行、列索引信息；
    如果提供 index 或 columns 项，其必须和data的行 或 列长度相同；
    如果不提供 index 或 columns 项，那么其将默认生成数值索引range(0, data.shape[0])) 或 range(0, data.shape[1])。
2.2 data无 行索引，有 列索引
    如果data为 dict of ndarray(1D) or list(1D)，所有ndarray或list的长度必须相同。且dict的key为DataFrame提供了需要的columns信息，缺失index；
    如果提供 index 项，必须和list的长度相同；
    如果不提供 index，那么其将默认生成数值索引range(0, data.shape[0]))；
    如果还额外提供了columns项，那么其将对当前构建的DataFrame进行 列重索引。
2.3 data有 行索引，有 列索引
    如果data为 dict of Series or dict，那么其已经提供了DataFrame需要的所有信息；
    如果多个Series或dict间的索引不一致，那么取并操作（pandas不会试图丢掉信息），缺失的数据填充NaN；
    如果提供了index项或columns项，那么其将对当前构建的DataFrame进行 重索引（reindex，pandas内部调用接口）。
3.1 csv创建
    pd.read_csv(filepath_or_buffer, sep=',', header='infer', names=None,index_col=None, encoding=None )
    read_csv的参数很多，但这几个参数就够我们使用了：
    filepath_or_buffer：路径和文件名不要带中文，带中文容易报错。
    sep: csv文件数据的分隔符，默认是','，根据实际情况修改；
    header：如果有列名，那么这一项不用改；
    names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引；
    index_col：int型，选取这一列作为索引。
    encoding：根据你的文档编码来确定，如果有中文读取报错，试试encoding = 'gbk'。
3.2 excel创建
    pd.read_excel(io, sheetname=0, header=0, index_col=None, names=None)
    read_excel的参数很多，但这几个参数就够我们使用了：
    header：如果有列名，那么这一项不用改；
    names：如果没有列名，那么必须设置header = None， names为列名的列表，不设置默认生成数值索引；
    index_col：int型，选取这一列作为索引。



"""
import pandas as pd
import numpy as np


def properties(series):
    print(series)
    print(series.index)
    print(series.name)
    print(series.values)
    print(series.dtype)


def builder(series):
    print(series)


if __name__ == '__main__':
    properties(pd.Series(data=[1, 2, 3], index= ['a', 'b', 'c'], name='series'))
    builder(pd.Series({1: 'a', 3: '5'}))
    builder(pd.Series([1, 3, 5, 7, 9]))

    dataFrame = pd.DataFrame(data=(['1', 'payno', 'male'],['2', 'taylar', 'female']),index=[1, 2],columns=['id', 'name', 'sex'])
    print(dataFrame)

    aumCsv = pd.read_csv('d:/aum.csv',encoding='gbk')
    print(type(aumCsv))
    print(type(aumCsv.head(2)))