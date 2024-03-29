"""
Title: File

Author: Bear Payne
Date: 2019/11/11 10:49
Description:
    'r' 	读取 （默认）
    'w' 	写入（会先截断之前的内容）
    'x' 	写入，如果文件已经存在会产生异常
    'a' 	追加，将内容写入到已有文件的末尾
    'b' 	二进制模式
    't' 	文本模式（默认）
    '+' 	更新（既可以读又可以写）
"""

if __name__ == '__main__':
    f = open('d:/random.txt','r',encoding='utf-8')
    print(f.read())

    f = None
    try:
        f = open('d:/random.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

    # 不就是Java里的TryWithResource
    try:
        with open('d:/random.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

    try:
        with open('d:/random.txt','rb') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')