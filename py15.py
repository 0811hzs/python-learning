#1.继承
#就是让类与类之间转变为父子关系，子类默认继承父类的属性和方法
#继承分为单继承和多继承
#1.1 语法：
# class 类名(父类名):
#      代码块
#1.2 单继承（可以是多个类是同一个类的子类)
# class  Person:#父类
#     name="bingbing"
#     def eat(self):
#         print("我会吃饭")
#     def sing(self):
#         print("我是唱歌小能手")
#
# class Girl(Person):#此时Girl就是person类的子类了
#     pass#占位符，代码中类下面不写任何东西，会走动跳过,不会报错
# class Boy(Person):#也是person类的一个子类
#     pass#类中不写代码的时候必须写pass不然会报错，占位符写None也可以
# girl=Girl()
# girl.eat()#我会吃饭
# print(girl.name)#bingbing
# boy=Boy()
# boy.sing()
# boy.eat()
#总结:子类可以继承父类的属性和方法(不是继承所有的是继承公共的和受保护的方法和属性）
#1.3继承的传递
#A/B/C三个类  C继承B类，B类继承A类，c类具有A类和B类所有的公共的这些属性和方法
# class Father:
#     def eat(self):
#         print("吃饭")
#     def sleep(self):
#         print("睡觉")
# class  son(Father):
#     def sing(self):
#         print("会跳舞")
# class sun(son):
#     None
# boy=sun()
# boy.eat()
# boy.sleep()
# boy.sing()

#1.4重写指在子类中定义与父类相同名称的方法
#1.4.1 覆盖父类方法
# class Father:
#     def money(self):
#         print("100万需要继承")
# class son(Father):
#     def money(self):
#         print("我挣了100万")
# boy=son()
# boy.money()#我又挣了100万
# fa=Father()
# fa.money()#100万需要继承

#1.4.2对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
#1.父类名.方法名(self)
#2.super().方法名() --推荐使用这种    ，懒人写法
#super(子类名,self).方法名（）
#super在python中是一个特殊的类，super()是使用super类创建出来的对象，可以调用父类中的方法
# class Father:
#     def money(self):
#         print("100万需要继承")
#     def sleep(self):
#         print("睡觉了")
# class son(Father):
#     def money(self):
#         #Father.money(self)#方法一
#         # super().money()#方法二
#         # super().sleep()#这个是子类中的函数中调用父类中的方法
#         super(son,self).money()
#         print("我挣了1000万")
# boy=son()
# boy.money()#我又挣了100万

#2.新式类写法
# class A: #经典类:不由任何内置类型派生出来的类
#     pass
# class Animal:
#     def walk(self):
#         print("走路")
# class Dog(Animal):
#       #pass  #不是派生类
#     def bite(self):
#         print("咬人")#此时就是派生类，因为他有父类没有的方法或属性
#2.2 class A（）
#2.3 class A(object) 新式类：继承了object类或者该类的子类都是新式类   --推荐使用这种
#object --对象，python为所有对象提供的基类（顶级父类），提供了一些内置的属性和方法，我们可以使用dir()来查看
# print(dir(object))
#object类是所有类的父类，在python中所有的类都继承object类
#在python3中如果一个类没有继承任何类，则默认继承object类，因此python3都是新式类
#总结：直接使用 class A：就行


#多继承   子类有一个父类叫单继承，子类有多个父类叫多继承，并且具有所有父类的属性或者方法
# class Father(object):
#     def eat(self):
#         print("吃顿饭")
#     def sing(self):
#         print("我不会唱歌")
# class Mom:
#     def sing(self):
#         print("唱首歌")
# class child(Father, Mom):
#     pass
# boy=child()
# boy.eat()
# boy.sing()#如果这多个父类中有重名的方法（函数），优先调用第一个父类中的该方法
#当然开发时要尽量避免这种情况
#3.3 方法的搜索顺序（了解）
#python中内置的属性__mro__可以查看方法搜索顺序
# print(child.__mro__)
#搜索方法时，会先按照__mro__的输出结果，先是从自身类找起，之后按照父类调用顺序从左往右的顺序查找，其实也就是调用父类的顺序，其实没事意思

#3.4多继承的弊端
#容易引发冲突
#会导致代码设置的复杂度增加

#4.多态
#指同一种行为具有不同的表现形式
#4.1多态的前提
#继承
#重写
# class Animal:
#     """父类：动物类"""
#     def shout(self):
#       print("动物会叫")
# class Cat(Animal):
#     """子类一：猫类"""
#     def shout(self):
#         print("小猫：喵喵喵")
# class Dog(Animal):
#     def shout(self):
#         print("小狗：汪汪汪")
# cat=Cat()
# dog=Dog()
# cat.shout()
# dog.shout()
#4,2 多态性：一种调用方式，不用的执行结果（说白了就是父类写个方法，子类继承并重写该方法，不同子类重写方式不同，输出结果自然就不一样)


#5静态方法
#使用@staticmethod来进行修饰，静态方法没有self.cls参数的限制
#静态方法与类无关，可以转换成函数来使用
# class Person:
#     @staticmethod
#     def study(name):#静态方法
#         print(f"{name}类会学习")
# #静态方法既可以使用对象访问也可以使用类访问
# Person.study("李华")
# pe=Person()
# pe.study("binging") #调用方法时传参数
#什么时间使用静态方法呢？逻辑上属于这个类，但不调用类属性也不调用实例属性的时候使用静态方法

#类方法
#使用装饰器@classmethod来标识为类方法，对于类方法，第一个参数必须是类对象，一般是以cls作为第一个参数
#cls指所在类的类本身，self指的是所在类创建出的实例化对象
# class 类名：
#      @classmethod
#      def 方法名(cls,形参):
#        方法体
class Person:
    def sleep(cls):
        print(cls)#输出<class '__main__.Person'>，这个cls就是所在类本身
        print("人类在睡觉")
Person.sleep()
#类方法和静态方法都可以由类名直接来调用，也可以通过实例对象来直接调用
pe=Person()
pe.sleep()
#类方法内部可以访问类属性，类属性可以直接拿来使用
#静态方法和类方法可以调用类中的实例方法，但不能直接调用，因为传进来的只有cls不是self，必须用cls().实例方法()的方式来调用

























