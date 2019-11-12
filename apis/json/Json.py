"""
Title: Json

Author: Bear Payne
Date: 2019/11/11 16:09
Description:
    dump - 将Python对象按照JSON格式序列化到文件中
    dumps - 将Python对象处理成JSON格式的字符串
    load - 将文件中的JSON数据反序列化成对象
    loads - 将字符串的内容反序列化成Python对象

    loads()传的是字符串，而load()传的是文件对象
    使用loads()时需要先读文件再使用，而load()则不用
    .dump()不需要使用.write()方法，只需要写哪个字典、哪个文件即可；而.dumps()需要使用.write()方法写入
    如果要把字典写到文件里面的时候，dump()好用；但如果不需要操作文件，或需要把内容存到数据库和Excel，则需要使用dumps()先把字典转成字符串，再写入

"""
import json

if __name__ == '__main__':
    file = open('d:/test.json','r',10,encoding='utf-8')
    str = file.read()
    dict0 = eval(str)
    for _ in dict0:
        print(f'key:[{_}],value:[{dict0.get(_)}]')
    jsonObj = json.loads(str)
    print(type(dict0))
    print(type(jsonObj))
