"""
Title: Index

Author: Bear Payne
Date: 2019/11/14 11:45
Description:
    data: Any = None,
          dtype: Any = None,
          copy: bool = False,
          name: Any = None,
          fastpath: Any = None,
          tupleize_cols: bool = True,
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


if __name__ == '__main__':
    # 构造方法
    index1 = pd.Index(['a', 'b', 'c'], dtype='object', name='name1')
    println(index1)

    # 查询索引
    println(index1[0])
    println(index1[[False,True,False]])
    println(index1[:2])

    # 改索引名字
    index1.name = 'payno'
    println(index1)
    index2 = index1.rename('payne')
    println(index2)
    index1.rename('payne', inplace=True)
    println(index1)

    # 增
    index3 = index1.insert(3, 'd')
    println(index3)

    # append,union immutable类型，所以是工厂方法
    index4 = index1.append(pd.Index(['g', 'h']))
    println(index4)