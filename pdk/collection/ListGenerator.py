"""
Title: ListGenerator

Author: Bear Payne
Date: 2019/11/11 08:53
"""
import sys

def listGenerator(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a

if __name__ == '__main__':
    ints = [x for x in range(1,100)]
    print(ints)
    strs = [x + y for x in 'ABCDEF' for y in '123456']
    print(strs)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    bigInts = [x ** 2 for x in range(1,1000)]
    print(sys.getsizeof(bigInts))
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    bigInts2 = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(bigInts2))
    # 相比生成式生成器不占用存储数据的空间

    for var in listGenerator(20):
        print(var)
