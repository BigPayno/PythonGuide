"""
Title: JsonPath

Author: Bear Payne
Date: 2019/11/11 16:22
Description:
JSONPath	描述
$ 	跟节点
@ 	现行节点
. or [] 	取子节点
n/a 	就是不管位置，选择所有符合条件的条件
* 	匹配所有元素节点
[] 	迭代器标示(可以在里面做简单的迭代操作，如数组下标，根据内容选值等)
[,] 	支持迭代器中做多选
?() 	支持过滤操作
() 	支持表达式计算
"""
import json
import jsonpath

def parse(path):
    data = eval(open('d:/test.json', 'r', encoding='utf-8').read())
    result = jsonpath.jsonpath(data, expr=path)
    print(f'jsonPath:{path}')
    print(f'value:{result}')

def get(path):
    data = json.load(open('d:/test.json','r',encoding='utf-8'))
    result = jsonpath.jsonpath(data, expr=path)
    print(f'jsonPath:{path}')
    print(f'value:{result}')
    print(type(result))

if __name__ == '__main__':
    # search
    parse('$..general_analyzed_data')
    get('$..general_analyzed_data')
    # list
    get('$..gjj_detail[*]')

