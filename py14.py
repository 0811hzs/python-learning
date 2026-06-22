#1.析构函数   __del__()
#删除对象的时候，解释器会默认调用__del__()方法
# class Person:
#     def __init__(self):
#         print("我是__init__()方法")
#     def __del__(self):
#         print("被销毁了")
# p=Person()
#del  p #删除p这个对象
#del  p 这句执行的时候，内存会立即被回收，会调用对象那本身的__del__()方法
# print("这是最后一行代码")
# # 我是__init__()方法
# 这是最后一行代码
# 被销毁了
#正常运行时不会调用__del__()函数，对象执行结束后，系统会自动调用__del__()函数
#__del__()主要是表示该程序或者函数已经全部执行结束


#2,封装
#面向对象的三大特性：封装，继承，多态
#封装：指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
# class Person:
#     name="bingbing"
# pe=Person()
# print(pe.name)
# print(Person.name)
#因为name是公共属性，可以由类名访问也可以由实例名来访问

#2.2 隐藏属性(私有权限）：只允许在类的内部使用，无法通过对象访问
# 在属性名或方法名前面加两个下划线__
# class Person:
#     name="bingbing"  #类属性
#     __age=18         #隐藏属性
#     def test(self):
#         Person.__age=120
#         print(f"{Person.name} is {Person.__age} years old.")
        #在实例方法中访问类属性和隐藏属性
# pe=Person()
# print(pe.name)
# pe.test()
#print(pe.age)#会报错，因为age是私有的类属性，只能在类中被访问
#第一种方式：了解
#隐藏属性实际上是将名字修改为：_类名__属性名
# print(pe._Person__age)#输出18
#第二种方式：在类的内部访问，推荐使用
# pe.test()


#2.3私有属性或者方法
#1.xxx:普通属性/方法 ，如果是类中定有的，则类可以在任何地方使用
#2._xxx:单下划线开头，声明私有属性或方法，如果定义在类中，外部可以使用，子类也可以继承
#       但是在另一py文件中通过from xxx import *导入的时候无法导入
#       一般是为了避免与python的关键字冲突而采用的命名方法
#3.__xxx:双下划线开头，隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承，要访问的话只能通过间接的方式
#        另外一个py文件中通过from xxx import * 导入的时候也无法导入
#        这种命名方法是python中的魔术方法/属性，都是有特殊含义或者功能的，自己不要轻易定义
# class Person:
#     name="泽省"
#     __age=22    #隐藏属性（双下划线开头）
#     _sex="男"   #私有属性（单下划线开头）
# pe= Person()
# print(pe._sex)#输出男
#2.4隐藏方法
# class Man:
#     def __play(self):  #隐藏方法方法
#         print("玩手机")
#     def funa(self): #平平无奇的方法
#         print("平平无奇的实例方法")
#         Man.__play(self)  #在实例方法中调用 隐藏方法    --不推荐
#         self.__play()  #推荐使用，更简便
# ma=Man()
# ma.funa()
#ma._Man__play()#输出玩手机

#2.5 私有方法
class girl:
    def _buy(self):
        print("整天买买买")
gi=girl()
gi._buy()#整天买买买

























































