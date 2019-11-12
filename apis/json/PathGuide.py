"""
Title: PathGuide

Author: Bear Payne
Date: 2019/11/11 17:10
Description:
    存在路径与不存在的情况  list,bool
    搜索的使用
    切片的使用
    过滤的使用
"""
import json
import jsonpath

def get(data,path):
    result = jsonpath.jsonpath(data, expr=path)
    print(f'{path}:')
    print(type(result))
    print(f'{result}')

if __name__ == '__main__':
    data = json.load(open('d:/test.json','r',encoding='utf-8'))
    # path exists
    get(data,'$..general_analyzed_data')
    get(data, '$..gjj_data[*].gjj_detail[0]')
    get(data, '$..gjj_account_analyzed_data.back_cont_last_times')
    # path does not exist=>bool False
    get(data,'$..payno')
    get(data,'$..payno.payno')

    # part
    get(data,'$..gjj_detail[*]')
    get(data, '$..gjj_detail[0]')
    get(data, '$..gjj_detail[-1:]')
    get(data, '$..gjj_detail[(@.length-1)]')

    # filter gjj_detail数组下的对象，存在gjj_type属性的对象
    get(data,"$..gjj_detail[?(@.gjj_type)]")


