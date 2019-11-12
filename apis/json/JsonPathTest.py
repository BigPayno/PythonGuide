"""
Title: JsonPathTest

Author: Bear Payne
Date: 2019/11/12 10:32
Description:
    由于python的jsonPath过于坑，建议人工判断是否是listWrapper
"""
import json
import jsonpath


def print_with_type(out):
    print(type(out))
    print(out)


def test(json_data,json_path):
    print(json_path)
    print_with_type(jsonpath.jsonpath(json_data,json_path))
    print('--------------------------------------------')


class Path(object):
    def __init__(self, json_data, json_path, is_list_wrapper):
        self.result = jsonpath.jsonpath(json_data, json_path)
        if isinstance(self.result, list):
            if is_list_wrapper is True:
                self.result = self.result[0]

    @staticmethod
    def of(json_data, json_path,is_list_wrapper):
        return Path(json_data, json_path, is_list_wrapper)

    def is_valid_data(self):
        # jsonPath解析路径不存在对应数据，返回False
        if self.result is False:
            return False
        # jsonPath存在对应路径，默认为list格式,在构造函数中已经提取出来了
        else:
            # 对于0，False进行单独判断，为有效数据
            if self.result == 0 or self.result is False:
                return True
            # 如果是空列表，字典，集合，None等，认为无效数据
            elif not self.result:
                return False
            else:
                # 对于str类型，NULL、BLANK认为是无效数据
                if isinstance(self.result, str):
                    return self.result.strip(' ') == ''
                return True


class PathBuilder(object):
    def __init__(self,json_data):
        self.json_data = json_data

    # 人工判断json path库最后是否用list包装了一层，还是java的相关库好用
    def build(self,json_path,is_list_wrapper):
        return Path.of(self.json_data, json_path, is_list_wrapper)


if __name__ == '__main__':
    data = json.load(open('d:/test.json', 'r', encoding='utf-8'))

    # 读取字段，对象，列表    如此奇怪的结果，只有.gjj_data符合预期
    # 对于非list类型，会包一层list，但是对于list除非不加[]之类的结果，又不包装一层
    test(data, '$.data.gjjData.orderId')
    test(data, '$.data.gjjData.data')
    test(data, '$.data.gjjData.data.gjj_data[:]')
    test(data, '$.data.gjjData.data.gjj_data[0]')
    test(data, '$.data.gjjData.data.gjj_data[*]')
    test(data, '$.data.gjjData.data.gjj_data')
    test(data, '$..gjj_data[*]')
    test(data, '$..gjj_data')

    # 读取列表中的字段，对象，列表
    test(data, '$.data.gjjData.data.gjj_data[0]..gjj_account_analyzed_data.back_sum_times')
    test(data, '$.data.gjjData.data.gjj_data[0]..gjj_brief')
    test(data, '$.data.gjjData.data.gjj_data[0]..gjj_detail')
    test(data, '$.data.gjjData.data.gjj_data[0]..gjj_detail[:]')
    test(data, '$..gjj_detail[:].record_date')

    # 使用
    gjjPathBuilder = PathBuilder(data)
    gjjDetailList = gjjPathBuilder.build('$.data.gjjData.data.gjj_data[0]..gjj_detail[:]', False)
    print_with_type(gjjDetailList.result)
    print(gjjDetailList.is_valid_data())
    loanDataList = gjjPathBuilder.build('$.data.gjjData.data.loan_data',True)
    print_with_type(loanDataList.result)
    print(loanDataList.is_valid_data())