#1.作用域
#1.1含义：指的是变量生效的范围，分为局部变量和全局变量
#在函数内部修改全局变量的值，可以使用global关键字、
#global
#作用：将变量声明为全局变量
#语法格式：global 变量名
## a=100
# def funa():
#     #global a=120#这个写法是不正确的，
#     global a
#     a=120
#     print("这是a的值：",a)
# funa()#这是a的值： 120
# print("a的值：",a)#a的值： 120
#1.2全局变量
#函数外部定义的变量，在整个文件中都是有效的
#1.3局部变量
#函数内部定义的变量，从定义位置到函数定义结束位置有效
#局部变量只能在被定义的函数中使用，函数外部不能使用
#作用：在函数体内部，临时保存数据，即当函数调用完成后即被销毁
# def study():
#     name="python基础"
#     print("我在学习",name)
# study()
# a=100
# names="bingbing"
# print(f"我的年龄{a},我的名字{names}")#这个必须加f
# def study():
#      global name ,age#global可以同时定义多个变量
#      name="bingbing"
#      age=20
#      print(f"{age}岁的我的名字是{name}")
# study()#必须先写study()，只有这样全局变量name才会被创建
# print(f"我的名字是{name}")
#总结：global关键字可以对全局变量进行修改，也可以在局部作用域中声明一个全局变量
#
from operator import ifloordiv
from selectors import SelectSelector

#1.5 nonlocal关键字 --了解
#用来声明外层的局部变量，只能在全套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明
# a=10 #全局变量
# def outer(): #外函数
#     a=5
#     def inner():
#         nonlocal a
#         a=20
#         print(f"inner函数中a的值是{a}")
#     inner()
#     print(f"outer函数中a的值是{a}")
# outer()#输出的是20 20
#总结：nonlocal只能对上一级进行修改



#2匿名函数
#2.1基本语法
# 函数名=lambda 形参：返回值（表达式）
#调用：结果=函数名（实参）

# def add(a,b):
#     return a+b
# print(add(1,2))
#匿名函数
# add=lambda a,b: a+b#a，b就是匿名函数的形参，a+b是返回值的表达式
# print(add(1,2))
#lambda不需要写return来返回值，表达式本身就是返回值

#2.2lambda的参数形式
#函数名=lambda 形参：返回值（表达式）
#无参数
# funa=lambda :"一桶水果茶"
# print(funa())#输出一桶水果茶

#2.2.2 一个参数
# funb=lambda name:name
# print(funb("bingbing"))
#2.2.3默认参数
# func= lambda name,age=18 :(name,age)#(name,age)这个是元组的形式，为什么要这样写呢，因为lambda的：后面只能有一个表达式，
# 要是不加括号的话就变成两个表达式了，这个是语法错误
#print(func("bingbning",20))
#默认参数必须写在非默认参数的后面
#2.2.4 关键字参数
# fund=lambda **kwargs:kwargs
# print(fund(name="bingbing",age=18))#输出{'name': 'bingbing', 'age': 18}，是个字典形式

#2.3 lambda结合if判断
# a=5
# b=8
#为真结果 if 条件 else 为假结果
# print("a<b") if a<b else print("a>b")#加“的话输出的是a<b或a>b，不加的话输出的是a<b的结果即true或false
# comp=lambda a,b:"a<b" if a<b else "a>b"
# print(comp(1,2))
# #缺点：lambda只能实现简单的逻辑，如果逻辑复杂且代码量大，不建议使用lambda，降低代码的可读性，为后期代码的维护增加困难

#3.内置函数
#3.1查看所有的内置函数
# import builtins
# print(dir(builtins))
#大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
#3.2内置函数一
#3.2.1 abs（）：返回绝对值
#3.2.2 sum（）：求和
#print(sum(123))#会报错，整形不是可迭代对象，sum函数内要放可迭代对象
# print(sum([1,3,4,4]))#输出12 ，[1,2,3]这是列表，（1，2，3）这是元组，{1，2，3}这是集合，这些都可以因为他们都是可迭代对象
#但是字符串不行
# print(sum({1.3,2,3}))#只要有一个是浮点数，运算结果就一定是浮点数

#3.3 内置函数2
#3.3.1 min（）：求最小值     max（）：求最大值
# print(min([1,2,4]))#输出1，min（）和max（）这括号中的可以是单个输入也就是可迭代对象 ，列表，元组，集合，也可以是多个对象
# print(min(1,2,3))#输出1
# print(max(-8,5,key=abs))#输出-8，传入求绝对值函数，则参数就会先求绝对值在去除最大者

#3.3.3 zip():将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li=[1,3,4,5]
# li2=['a','b','c']
# print(zip(li,li2))
#第一种方式：通过for循环
# for i in zip(li,li2):
#     print(i)
#     print(type(i))#输出内容如下,只会从前到后一一对应
#(1, 'a')#这是元组的形式
# <class 'tuple'>
# (3, 'b')
# <class 'tuple'>
# (4, 'c')
# <class 'tuple'>
#如果元素个数不一致，就按照长度最短的返回

#第二种方式：转化成列表打印
# print(list(zip(li,li2)))#转换成列表打印
#注意，必须是可迭代对象

#3.3.4 map（）函数：可以对可迭代对象中的每一个元素进行映射，分别去执行
#map（func，iter1）：func--自己定义的函数，iter1--要放进去的可迭代对象
#简单来说就是对象中的每一个元素都会去执行这个函数
#li=[1,2,3]
# def funa(x):
#     return x*5
# funa =lambda x:x*5#这是使用匿名函数来替代上述完整函数
# mp=map(funa,li)#注意：只需要写函数名，不需要加（）
# print(mp)#输出<map object at 0x000001B94BA6B440>
#方法一
# print(list(mp))#输出[5, 10, 15]
#方法二
# for i in mp:
#     print(i)
#方法一和方法二对同一个变量只能同时用一个方式进行输出，因为map函数操作后，形成的是一个迭代器，只能被消耗一次，消耗完了就没了

#3.3.5 reduce（）：先把对象中的两个元素取出来，极计算出一个值然后保存着，接下来把这个计算值与第三个元素进行计算
#需要先导报
from functools import reduce
#reduce依次循环直到可迭代对象中只剩一个元素为止，这就是最终结果

#4.拆包
#含义：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
tua=(1,2,3)#这是一个元组
# print(tua)
# print(tua[1])
#方法一
# a,b,c=tua
# print(a,b,c)
#要求元组内的个数与接受的变量个相同，对象内有多少个数据就需要定义定义多少个变量来接受
#一般在获取元组值的时候使用

#方法二
# a,*b=tua
# print(a,b)#输出1 [2, 3]
# #一般在函数调用时使用
# tub=(1,2,3,4,5,6)
# def funa(a,b,*args):
#     print(a,b)
#     print(args,type(args))
# funa(1,2,3,4,5,6)