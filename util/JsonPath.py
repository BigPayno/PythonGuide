"""
Title: JsonPath

Author: Bear Payne
Date: 2019/11/12 11:08
Description:
    
"""
import json
import jsonpath


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
    def build(self, json_path, is_list_wrapper):
        return Path.of(self.json_data, json_path, is_list_wrapper)