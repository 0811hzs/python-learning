#1.抛出异常
#步骤：
#1.创建一个Exception（”xxx“）对象，xxx是异常提示信息
#2.raise抛出这个对象（异常对象）
#raise Exception("bingbing抛出了一个异常")#raise是python关键字，用于手动出发异常
#Exception表示一般性的错误
# def func():
#     print("hahaha")#
#     raise Exception("抛出一个异常")#抛出异常后，寻找匹配的 try...except 块去捕获这个异常,如果一直没被捕获，程序最终会终止并打印异常信息
# func()
# hah=lambda x,y:x*y
# print(hah(2,3))#因为上述异常抛出后未曾找到try，所以该部分代码不会被执行

#需求：密码长度不足就报异常
#分析：用户输入密码，密码长度小于6位就报错，即抛出自定义异常，并捕获该异常
# def login():
#     pwd=input("请输入密码：")
#     if len(pwd)>=6:
#         print("密码输入成功")
#     else:
#         raise Exception("输入密码位数不足")
# login()
# try:
#     login()
# except Exception as e:
#     print(e)
#捕获异常是为了检测到异常时代码还能继续往下运行，即程序不会终止
#请输入密码：123
#输入密码位数不足
# print("1234")#此时虽然上面报错但这个还能运行

#2.模块
#2.1 含义：一个py文件就是一个模块，即导入一个模块本质上就是执行一个py文件
#2.2 分类：
#2.2.1 内置模块
#如random ，time，os，logging，直接导入即可使用
import time #这样并不会报错
#2.2.2 第三方模块（第三方库）
#下载：cmd窗口输入pip install 模块名
#3.2.3 自定义模块
#即自己在项目中定义的模块
#注意:命名要遵循标识符规定以及变量的命名规范，并且不要与内置模块起冲突，否则将导致模块功能无法使用
#3.3导入方式
#3.3.1 import 模块名
#语法：
#导入模块方式一
#import 模块名1，模块名2#可以通过这种方式同时导入多个模块，但最好还是单独导入（即一个模块一个模块的导入）
#调用功能：
#模块名.功能名
# import pytest#导入任何一个模块，事实上都是先执行一遍该模块（就是从上到下执行所有可以执行的语句）
# pytest.funa()#输出这是pytest模块中的funa（）函数
# print(pytest.name)#输出bingbing
#3.3.2导入模块方式二  from.....import....
#语法:
#从模块中导入指定的部分
# from 模块名 import 功能1,功能2....
#调用功能：
#直接输入功能名即可，不需要添加模块名
# from pytest import funa,funb,name#导入的时候只需要函数名不需要小括号，但调用的时候需要小括号
#不同模块中的函数名可以相同，调用不同模块中同一函数时后调用的函数会覆盖原模块的该函数
# print(name)#如果没有导入就会报错
# funa()
#3.3.3方式三：from.....import *
#语法： from 模块名 import *#把模块中的所有内容全部导入
# from pytest import *
# funa()
# funb()
# print(name)
#注意：不建议过多使用from...import...声明，有时候命名冲突会产生一些错误
#3.3.4 as起别名
#1.as给模块起别名
#import 模块名 as 别名
#给模块起别名
#import pytest as pt
#调用模块中的funa（）
# pt.funb()#输出这是pytest模块中的funb（）函数
# print(pt.name)#输出bingbing
#2.as给功能起别名
#语法：from 模块名 import 功能 as 别名
# from pytest import funa as  func,name#改名字只写名字就好了，不用写（），（）是调用的时候才写的
#上述这种虽然只调用模块中一个函数并改名，但是和调用整个模块是一样的都会运行被调用的整个模块的代码
# func()#输出：这是test模块
# 123
# 这是pytest模块中的funa（）函数
# print(name)#bingbing
#注意：导入多个功能，使用“，"将功能与功能隔开，后面的功能也可以取别名：功能名 as 别名

#3.4 内置全局变量__name__
#3.4.1 语法：
#if __name__=="__main__":
#3.4.2 作用
#用来控制py文件在不同的应用场景执行不同的逻辑
#3.4.3 __name__
#1.文件在当前程序执行（即自己执行自己）：__name__=="__main__"#这句的意思是，只有当前文件是程序入口，单独运行时才会执行下面的代码，
# 被其他模块等调用的时候不会执行下述代码，所以这个就可以使别人看不到被调用模块不想让别人看到的信息
#2.文件被当作模块被其他文件导入：__name__==模块名
#import pytest2

#包
#4.1含义：就是项目结构中的文件夹或者目录
#4.2 与普通文件夹的区别:包是含有__init__.py的文件夹
#4.3 作用：包就是将有联系的模块放到同一个文件夹下，有效避免模块名称冲突问题，让结构更清楚
#4.4建立包的话是new python package
#建立普通文件的话是new directory
#4.5 import导入包时，首先执行__init__.py文件的代码
#导包方式一
#import pack_01#输出这里是pack_01的__init__.py文件
#就是只执行包中的__init__.py文件，该包内的其他文件不调用也不执行
#导包方式二
#from pack_01 import register#默认执行pack_01的__init__.py文件
#register.reg()
#4.6 不建议在__init__文件中编写过多代码，尽量保证init文件的内容简单
#可以直接在包的__init__文件中导入该包中的其他模块，这样其他文件调用该包内的其他模块时就不用在写调用代码了
import pack_01
#输出这里是pack_01的__init__.py文件
#这里是登陆函数
#4.7 __all__:本质上是一个列表，列表里面的元素就代表要导入的元素
# 可以控制要引入的东西
from pack_01 import *#这个是和2__all__=[]结合使用的[]中有什么模块，*才会调用哪些模块
#输出：这里是登陆函数，为啥会输出这个呢，因为每调用一个模块都会先执行该模块中的所有代码
#调用方式：
register.reg()#这种方式就不需要加pack_01.了
login.log()













