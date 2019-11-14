"""
Title: FunctionalProgram

Author: Bear Payne
Date: 2019/11/14 15:17
Description:
    
"""
import pandas as pd


def println(word):
    print(word)
    print(type(word))
    print()


def print_t(obj):
    println(type(obj))


class Num(object):
    number = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    @staticmethod
    def toshr(number):
        string = str(number)
        result = ''
        for x in range(0,len(string)):
            result +=Num.number[int(string[x])]
        return result


if __name__ == '__main__':
    series = pd.Series([122, 2, 45, 3, 33, 9])
    series.index = series.map(Num.toshr)
    println(series)
    # Series 的filter是对index进行操作
    series.filter(items={'二'}, axis=0).apply(println)
    series.filter(like='三', axis=0).apply(println)
    # series.filter(regex='', axis=0).apply(println)

    table = pd.DataFrame(data=[[22, 'male', 'payne'], [23, 'female', 'taylor'], [15, 'male', 'zd'], [11, 'male', 'zy']],
                         columns=['age', 'gender', 'name'])
    println(table[table['gender'].str.contains('female')])
    println(table[table['age'] > 20])