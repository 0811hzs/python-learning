# class Person:
#     name="bingbing"#类属性
#     def __init__(self):#该函数在构造实例化对象的时候会自主执行
#         self.age=18  #这是实例属性 ，实例方法中定义的属性成为实例属性
#     def sleep(self):
#         hi=100   #普通的局部变量
#         print(Person.name,hi)#实例化函数中访问类属性
#         print(self.age)#这个可以直接输出，因为age是实例化属性
#     @staticmethod
#     def sing(wi):
#       #print(Person.sleep.hi)#这个不行，变量不能访问，属性可以访问对吧
#       print(f"{Person.name}的体重是{wi}斤")
#     @classmethod
#     def song(cls):
#         print(f"{cls.name}")
# pe=Person()
# pe.sleep()
# pe.sing(200)
# pe.song()
#总结：类属性是公共的，类中所有的方法都可以访问他，但实例属性只有实例方法方便访问，因为只有实例方法才有实例对象self，否则也能访问不过需要创建个实例化对象门之后间接的来调用实例化属性


#1.__init__()和__new__()
#1.1__init__():初始化对象
#1.2__new__():object基类提供的内置的静态的方法
#作用：1.在内存中为对象分配空间，2.返回对象的引用
# class Test:
#     def __init__(self):
#         print("这是__init__方法")
#     def __new__(cls, *args, **kwargs):
#         # print("我是__new__（）函数") #这里直接写会将方法覆盖掉，使其失去原有的功能，，此时就需要对功能进行扩展
#         re=super().__new__(cls)#方法重写，re里面保存的是实例对象的引用，这个cls必须写因为这个标识着给谁分配空间并返回对象
#         #                       __new__()是静态方法，形参里面有cls，实参里就必须传cls
#         print("这是__new__()函数")
#         return re  #这个需要作为返回值进行返回
#         #注意：重写__new__()一定要return super().__new__(cls),不然python解释器得不到分配空间的对象引用，就不会调用之后的__init__()函数
# te=Test()
# print(te)
#实例化对象的过程中会调用__init__()这个方法，但不是最先调用，__new__()方法比他先调用
#执行步骤
#一个对象的实例化过程：首先执行__new__(),如果没有重写__new__()函数，就默认调用objectic里面的__new__()函数
#返回一个实例对象，然后再去调用__init__()函数，对对象进行初始化
# class Person:
#     def __new__(cls, *args, **kwargs):
#         print("这是new方法")
#         print(super().__new__(cls))#这个输出的结果和print(pe)输出的结果相同，说明，super().__new__(cls)返回的就是个实例化对象本身
#         return super().__new__(cls)  #super()就是父类的意思，在这里指的是objectic类
#     def __init__(self,name):
#         self.name=name #实例属性
#         print("名字是:",self.name)
# pe=Person("bingbing")
#总结:__new__()和__init__()
#1.__new__()是创建对象并返回对象，__init__()是初始化对象并定义实例属性

#2.单例模式
#2.1可以理解成一个特殊的类，这个类只存在一个对象，就是说之后创建的对象跟第一次创建的对象是一样的
#我们正常书写不是单例模式，正常写的话每次都会生成新的对象，要写成单例模式也就是每次都创建为同一个对象的话，需要重写__new__()函数才行
# class Singleton:
#     _instance = None  # 存唯一实例
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)  # 第一次才创建
#         return cls._instance  # 之后都返回同一个
# s1 = Singleton()
# s2 = Singleton()
# print(s1 is s2)  # True，s1 和 s2 是同一个对象
# class A:#默认继承的是objectic基类
#     pass
# a1=A()
# print(a1)
# a2=A()
# print(a2)
#上述两个输出不同，说明不是同一对象，不是单例模式（每次生成的地址都是一样的)
#__new__()方法返回地址的引用就是内存地址
#所以通过重写new方法可以实现单例模式
#设计流程
#1.定义一个类属性，初值为None，用来记录单例对象的引用
#2.重写new方法
#3.进行判断，如果类属性是None，把__new__()返回的对象引用保存进去
#4.返回类属性中记录的对象引用
# class singleton:
#     home=None
#     def __new__(cls, *args, **kwargs):
#         if cls.home is None:
#             cls.home=super().__new__(cls)
#         return cls.home
#     def __init__(self):
#         print("我是init函数")
# h1=singleton()
# h2=singleton()#只要__new__()函数能顺利返回对象，__init__()函数就可以顺利执行
# print(h1)
# print(h2)
#优点：省资源，全局只有一个入口

#3.魔法方法：
#在python中，__xx__()的函数叫魔法函数，指的是具有特殊功能的函数
#3.1 __doc__():类的描述信息，这个魔法函数输出的就是""""""中写的类的描述信息
# class Person:
#     """人类:类的描述信息"""
#     pass
# pe=Person()
# print(pe.__doc__)#输出人类:类的描述信息
# def sing():
#     """唱歌"""
#     pass
# print(sing.__doc__)
#3.2__model__():表示当前操作对象所在的模块
#3.3__class__():表示当前操作对象所在的类
# import pytest
# pe=pytest.Person()#调用其他模块中的函数的时候，需要使用模块名.方法名()的方式来调用
# print(pe.__module__)#pytest
# print(pe.__class__)#<class 'pytest.Person'>
#3.4__str__():对象的描述信息
#如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中return的数据
#__str__()方法必须返回一个字符串
# class Person:
#     def sleep(self):
#         print("我不爱谁懒觉")
#     def __str__(self):
#        str= super().__str__()
#        return str+"我是__str__()函数"#这个方法必须要有返回值，并且一定是字符串类型
# pe=Person()
# print(pe)#单独输出pe和调用__str__()函数的返回结果是相同的，所以说单独调用__str__()函数没什么意义，所以一般重写该方法来输出描述信息
# print(pe.__str__())#跟print(pe)输出结果是一样的，因为执行print(pe)的时候底层调用的也是pe.__str__()方法
#3.5__del__()函数：析构函数，该函数是释放资源的用处，一般 del obj， obj=None 或者函数结束使用了就都会调用del方法
#3.6__call__():使一个实例对象成为一个可调用对象，就像函数那样可以调用
#可调用对象：函数/内置函数和类都是可调用对象，凡是可以把一对()应用到某个对象身上都可以称之为可调用对象
#callable():判断一个对象是否是可调用对象
# def funa():
#     print("hello")
# funa()
# print(callable(funa))#True,这是个可调用对象
# name="bingbing"
#name()#这个肯定是报错的，因为目前只是一个参数
# print(callable(name))#输出false
#
# class Person:
#     def __call__(self,name):
#         print(f"你好，{name}")
# pe=Person()
# pe("小明")
# pe.person()这个是在pe中找person这个函数，显然找不到会报错，想使用__call__()函数，需要实例化对象+()就好了
# class Person:
#     def name(self):
#         print("我的名字是泽省")
#
#     # 我们给 Person 加上 __call__ 方法
#     def __call__(self):
#         print("哈哈，我被当作函数调用了！")
#
#
# pe = Person()
#
# # 1. 访问并调用 pe 身上的 name 方法
# pe.name()
# # 输出：我的名字是泽省
#
# # 2. 直接调用 pe 对象本身（触发 __call__）
# pe()
# # 输出：哈哈，我被当作函数调用了！
#
# # 3. 你之前的写法（依然是报错）
# pe.person()
# # 依然报错：AttributeError，因为 pe 身上根本没有 person 这个属性






























