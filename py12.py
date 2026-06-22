#1.递归函数：入砂锅一个函数在内部不调用其他函数，而是调用它本身的话，这个函数就是递归函数
#1.1条件：
#      1.必须有一个明确的结束条件---递归出后
#      2.每进行更深一层的递归，问题规模相比上次递归都要有所减少
#      3.相邻两次重复之间有紧密的联系
#使用普通函数来写（实现1到100累加和）：
# def add():
#    s=0
#    for i in range(1,101):#range（）函数包前不包后
#        s+=i
#    print(s)
# add()
# def add2(n): #要累加到第n项
#     #如果是1，就直接返回1，--明确的结束条件
#     if n==1:
#         return 1
# return n+add2(n)#会报错，超出了最大深度
    #如果不是1，就重复执行累加并返回结果
#     return n+add2(n-1)
# print(add2(100))
#from collections.abc import async_generator

#斐波那契数列
#1 1 2 3 5 8 13 .....
# def funa(n):
#     if n==1 or n==2:
#         return 1  #这里就是明确的结束条件
#     else :
#         return  funa(n-1)+funa(n-2)
# print(funa(4))
# 1.3优点
#简洁，逻辑清晰，解题更具有思路
#1.4 缺点
#使用递归函数的时候，需要反复调用函数，耗内存，运行效率低



#2.闭包
#含义：在嵌套函数的前提下，内部函数使用了外部函数的变量，而且内部函数返回了外部函数，我们就把外部函数变量的内部函数称为闭包
#在嵌套结构（在函数中在定义函数）中内部函数使用外部函数的变量，并且外部函数返回的是内部函数本身，这是所谓的闭包
# def outer():
#     num=5
#     def inner():
#         print(num)
#         return num#这个return有没有都可以，没有的话就默认返回None，有的话就就返回具体数值
#     return inner
# print(outer())#返回的是内部函数的内存地址
# print(outer()())
# 分步拆解：
# 1. outer() → 拿到 inner 函数
# 2. outer()() → 调用 inner()
#    inner 内部执行 print(num) → 控制台打印数字 5
# 3. inner 函数没写任何 return，Python 所有函数默认返回 None
# 4. 外层 print() 把 inner 的返回值 None 打印出来
#第二种写法：
# ou=outer() #调用外函数
# ou()  #这是调用内函数

# def outer(m): #外函数，m是形参，也是外函数的局部变量
#     n=10
#     def inner(o):#内函数
#         print(f"计算结果：{m+n+o}")
#     return inner  #返回函数名，而不是inner（），因为inner函数里面参数比较多时或者说受限制时，写法不太规范
# outer(20)#运行后没有任何结果，因为outer只是return一个东西，本身并不输出
# print(outer(20))#这就有结果了，输出的是内函数的地址
# print(outer(20)(20))#输出30和None因为没有return，没有return的话就默认输出None

#2.2函数引用
# def funa():
#     print("hello")
# funa()#这个是在调用这个函数#hello
# print(funa)#这个是在输出函数所在位置#<function funa at 0x00000244F471F5E0>
# id():判断两个变量是否是同一个值的引用
a=1 #a只不过是一个变量名，存的是1所在的内存地址，就是a里面存了数值1的引用
# print(a)
# print(id(a))
# a=2
# print(id(a))#这个id返回的是1和2的地址不是a的地址#输出140710451643544
# print(id(2))#输出140710451643544
# def test1():#test1只不过是一个函数名，里面存了这个函数所在位置的引用（起始就是存的是test1这整个函数体的地址）
#     print("这是test函数")
# print(test1)#输出的就是test1整个函数的地址

#2.3 每次开启内函数都在使用同一份闭包变量
# def outer(m):
#     print("outer()函数中的值",m)
#     def inner(n):
#         print(f"inner()函数中的值{n}")
#         return n+m
#     return inner
# print(outer(10)(20))#第一个括号调用外函数，第二个括号调用内函数
# ou=outer(10)
#第一次调用
# print(ou(20))
#第二次调用
# print(ou(30))
#第三次调用
# print(ou(40))
#总结：使用闭包的过程中，一旦外函数被调用一次，返回了内涵数的引用（就是内函数的地址），虽然每次调用内函数，都会开启一个函数，但执行后都会消亡
#    实际上闭包变量只有一份，每次开启内函数都在使用同一份闭包变量

#4.装饰器
# def test02():
#     print("发送信息给冰冰")
# def test(fn):
#     print("开始注册")
#     fn()
# test(test02)
#将新功能函数作为参数传给原函数
#作用：在不改变原有代码的情况下给函数添加新的功能
#条件：
#    1.不修改原程序或函数的代码
#    2.不改变程序或函数的调用方法
#含义:装饰器本质上就是一个闭包函数，他的好处就是在不修改原有代码的基础上，增加额外的功能
#4.2标准版装饰器
# def send():
#     print("发送消息")
# def send2():
#     print("发红包")
# def funa(fn):
#     def inner():
#      fn()#执VB VBBBBBBBBB行被装饰的函数

#      return  "登录"
#     return inner
# print(funa(send)())
#4.3 语法糖
#格式：@装饰器名称
#return inner
#@outer#此处不能加（），加了（）就是对装饰器的执行，不加就是对装饰器的引用
#上述这个必须顶格写
# def send():
#     print("发送消息，笑死我了")
# print(outer(send))
# print(outer(send)())
#send() #此刻的执行过程就是执行的是outer（）函数，将其中的fn（）化成send（）函数,因为他会先读取@outer（）,就会先执行他
# @outer
# def send2():
#     print("发送消息")
# send2()
#前面这写被装饰的函数都是没有参数的
#4.4被装饰的函数有参数
# def outer(fn):
#     def inner(name):#name 是内函数的形参
#         print(f"{name}是inner函数中的参数")
#         fn(name)
#     return inner
# @outer
# def  func(name):
#     print("这是被装饰的函数")
# func("李华")
# 上述解释：@outer相当于是outer(func）返回的是inner对象，这一步是在调用外函数，返回的是inner，之后运行的实际是inner(name),这个"李华“就是name

#4.5被装饰的函数有可变参数*args（可变参数），**kwargs（关键字参数）
# def func(*args,**kwargs):
#     print(args)#元组（）的形式
#     print(kwargs)#字典{}的形式
# #func(1,2,3,name="bingbing",age="18")#name="bingbing"是关键字参数
# #输出(1, 2, 3)
# # {'name': 'bingbing', 'age': '18'}
# def outer(fn):
#     def inner(*args,**kwargs):
#         fn(*args,**kwargs)
#         print("这里是内函数")
#     return inner
# outer(func)(1,"susu",3,name="bingbing",age="18")
#输出：(1, 'susu', 3)
# {'name': 'bingbing', 'age': '18'}
# 这里是内函数
#4.6多个装饰器    #其实装饰器本质就是闭包 ，不过就是在闭包的基础上填加了一些功能
#第一个装饰器
def deco1(fn):
    def inner():
        return "哈哈哈"+fn()+"呵呵呵"
    return inner
#第二个装饰器
def deco2(fn):
    def inner():
        return "奈斯"+fn()+"非常优秀"
    return inner
#第三个装饰器
def deco3(fn):
    def inner():
        return "牛逼"+fn()+"666"
    return inner
#被装饰的函数一
@deco1
@deco2
@deco3
def test1():
    return "晚上在学习python基础"
print(test1())#哈哈哈晚上在学习python基础呵呵呵
#输出：哈哈哈奈斯晚上在学习python基础非常优秀呵呵呵
#多个装饰器的装饰过程，里函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程
