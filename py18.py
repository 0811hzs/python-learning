#1.可迭代对象,Iterable
#凡是可以被for循环遍历取值的都是可迭代对象
#遍历（迭代）：一次从对象中把一个个元素取出来的过程
#数据类型：str(字符串)，list（列表）[]，tuple（元组）()，dict（字典）{}，set（集合）{},区别字典是是“name"=”bingbing"这种的，但集合种是“name”，18 .29这样的
#1.2可迭代对象的条件
#1，对象实现了__iter__()方法
#2,__iter__()方法返回了迭代器对象
#__iter__()方法是python迭代器协议方法，当你对一个对象使用 for x in obj: 时，Python 内部会调用 obj.__iter__() 来获取迭代器
# f={"name":"bingbing","age":18}
# for i in f:
#     print(i)
#1.3 for循环工作原理
#1.先通过__iter__()获取可迭代对象的迭代器
#2，对获取到的迭代器不断调用__next__()方法来获取下一个值并将其赋值给临时变量
#1.4isinstance():判断一个对象是否是可迭代对象或者是一个已知的数据类型
#导入模块
# from collections.abc import Iterable#导入模块
# from typing import Iterator

#isinstance(o,t)o是对象，t是类型，可以是直接或者间接类名，基本类型或者元组
#instance函数不仅可以用于判断是否属于某个类型还可以用于判断时候属于某个类或某个类的子类
# st="123"
# print(isinstance(st,Iterable))#为啥这个输出的是True呢，是因为“”中的数字就不再是整数了，而是字符串类型
# # print(isinstance("123",(int,dict)))#False这个判断的是"123"是不是int或dict类型中的一种，若是其中一种的话就输出Ture

#2.迭代器
#是一个可以记住遍历位置的对象:在上次停留的位置就绪做后面的事情
#1.先通过iter()获取可迭代对象的迭代器
#2，next（）:一个个去取元素，取完元素后会引发一个异常
# li=[1,2,3,4,5]
# #不使用for循环了，使用上述两个方法来实现取出元素
# #1，创建可迭代对象 iterator迭代器对象，iterable是迭代器本身
# li2=iter(li)
# print(li2)#<list_iterator object at 0x000002207A0705E0>list_iterator object 表示这是列表迭代器对象
# #2，获取下一条数据
# print(next(li2))#输出1
# print(next(li2))#输出2，在当前位置寻找之后的对象
#取完元素后，再使用next()函数会引发StopIteration异常
#2.2可迭代对象Iterable迭代器Iterator
#作用于for循环的是可迭代对象（就是例如li是可得带对象，那么for循环就可作用于他
#作用于next的是迭代器
from collections.abc import Iterable
from collections.abc import Iterator
# name="bingbing"
# print(isinstance(name,Iterable))#判断是否是可迭代对象,True
# print(isinstance(name,Iterator))#这个用于判断是否是迭代器，False
# name=iter(name)#将name这个迭代器对象编译为迭代器
# print(isinstance(name,Iterable))#判断是否是可迭代对象,True
# print(isinstance(name,Iterator))#这个用于判断是否是迭代器，True
# 此时name即是迭代器对象也是迭代器
#总结：迭代器对象不一定是迭代器，但可以转化为一样的，说明迭代器对象一定是可迭代对象
#如果一个对象具有__iter__()方法那么是可迭代对象，要是有__iter__()方法和__next__()方法，那么是迭代器对象
#dir():可以查看对象的所有属性和方法，可以通过输出的方法来判断具体是可迭代对象还是迭代器对象
# print(dir(name))

#2.3迭代器协议
#对象必须提供一个next方法，执行该方法要么就返回迭代中的下一项，要么就引发stopIteration异常，来终止迭代

#2.4 自定义迭代器类
#两个特性：一个是__iter__()和__next__()
# class MyIterable():
#     def __init__(self):
#        self.name=1
#        print(self.name)
#     def __iter__(self):
#         return self#返回的是当前迭代器类的实例对象
#     def __next__(self):
#         if self.name==10:
#             raise StopIteration("终止迭代没有数据了")
#         self.name+=1
#         return self.name
# li=MyIterable()
# # print(isinstance(li, Iterable))
# for i in li:
#     # if i>10:
#     #     break
#     print(i)

#3.生成器 generator  （一种特殊的迭代器，可以理解为可以按需生成数据的工厂)
#普通的列表或元组在创建时，必须把所有数据一次性算出来并全部保存在内存里；而生成器不会一次性生成所有数据，它是边循环边计算（惰性计算），每次只生成一个数据，用完之后立刻释放内存。
#python中一边循环一边计算的机制，叫做生成器
#3.1 生成器表达式
#列表推导式
# for i in range(5):#range(5)其实是从0到4
#     print(i)
li=[i*5 for i in range(5)]#这个是列表推导式
gen=(i*5 for i in range(2))#生成器表达式
# print(li)#[0, 5, 10, 15, 20]
# print(gen)#<generator object <genexpr> at 0x0000020E50BD0E10>说明这是个生成器类对象
# print(next(gen))#输出0
# print(next(gen))#输出5
# print(next(gen))#超出已有数据的输出之后会报StopIteration错误
#3.2生成器函数 generation
#python中，使用了yield关键字的函数就称之为生成器函数
#yield的作用:
#1.类似于:return ,将指定值或者多个值返回给调用者
#2.yield语句一次返回一个结果，在每个结果中间，挂起函数，执行next（），在重新从挂起点继续往下执行
# #       是函数中断，并保存中断的状态
# li = []
# def test():
#     # global li#global关键字的作用：在函数内部声明某个变量是全局变量
#
#     li.append("a")
#     print(li)
# test()
# test()
#yield关键字会让一个函数从普通函数变成生成器函数
# def gen():
#     print("开始了")
#     yield "a"#第一次执行该函数会返回a，之后就不在往下执行了
#     yield "b"#第二次执行会返回b，是在上次执行位置基础上进行执行的
#     yield "c"#yield：像是一个“暂停键”。当代码执行到 yield 时，函数会暂停，把 yield 后面的值返回给外面；下次再调用时，
#     # 它会从上次暂停的地方继续往下执行，而不是从头开始
#     yield "d"
# g=gen()
# print(g)#<generator object gen at 0x0000018ACFA9B040>说明是生成器对象
# print(next(g))
# print(next(g))
# def gen2(n):
#     li=[]
#     # for i in  range(n):
#     #  li.append(i)
#     a=0
#     while a<n:
#         li.append(a)
#         yield a #执行完这句先暂停，并把a给return出来
#         a+=1
#     print(li)
# g2=gen2(5)#实例化普通函数这个对象其实就是函数调用后返回出的结果
# #         但普通函数中添加yield关键字之后就是生成器函数了不是普通函数了，实例化的这个对象是生成器不再是函数运行后的结果了
# print(g2)#<generator object gen2 at 0x0000028BBADFEC00>
# for i in g2:
#  print(i)#[0, 1, 2, 3, 4]

#可迭代对象+__next__()方法就是迭代器，迭代器+yield关键字就是生










