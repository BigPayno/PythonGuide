"""
Title: JsonPathGuide

Author: Bear Payne
Date: 2019/11/11 17:48
Description:
    python的jsonPath令人质疑
"""
import json
import jsonpath


def print_with_type(out):
    print(type(out))
    print(out)


class Path(object):
    def __init__(self, json_data, json_path):
        self.result = jsonpath.jsonpath(json_data, json_path)
        if isinstance(self.result, list):
            self.result = self.result[0]

    @staticmethod
    def of(json_data, json_path):
        return Path(json_data, json_path)

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
                else:
                    return True


if __name__ == '__main__':
    data = json.load(open('d:/test.json', 'r', encoding='utf-8'))
    print(Path(data,'$..comments').is_valid_data())
    print_with_type(jsonpath.jsonpath(data,'$..gjj_detail[*]'))
    print_with_type(jsonpath.jsonpath(data, '$..company_deposit_amount'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data[0]'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data[*]'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data.gjj_brief.company_deposit_amount'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data[0].gjj_brief.company_deposit_amount'))
    print_with_type(jsonpath.jsonpath(data,'$.data.gjjData.data.gjj_data[*].gjj_brief.company_deposit_amount'))


