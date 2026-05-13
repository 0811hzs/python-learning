from binascii import a2b_hex  # print("hello")
# # num1=3#定义位置的前面不能有空格
# # num2=4;
# # print(num1)
# # print(num2)
# # print(num1+num2)
# # #ctrl+/是给选中部分加#即注释
# # total=num1+num2;
# # print(total)
# # a="哈哈" #定义类型可以是任何类型
# # print(num1)
# # print(a)
# # print(type(num1))
# # # print(type(a))#type是判断变量类型的函数
# # six=1
# # six_=1
# # _six=1#标识符不能以数字开头
# #2.数值类型
# #
# # #2.1 整数类型
#
# # a=1
# # print(a)
# # print(type(a))
# # #2.2浮点类型
#
# # a=2.12
# # print(a)
# # print(type(a))
# # #2.3 bool类型 有严格的固定写法
#
# # print(type(True))
# # print(type(False))
# # #bool型可以当成整数对待，True相当于是1，false相当于是0
# # print(False+True)
# # print(False+1)
# # print(True-False)#像这些False与True与数字1和0相互加减之后得到的都是数字
# # #2.4 complex复数形
# # a=2+2j
# # b=3+4j
# # print(a+b)#实部与虚部其中虚部部分只能是j
#
# #4 字符串
# # """
# # a="haha"
# # b='haha'
# # print(a)
# # print(b)
# # # print(c)"""
# #对于字符串的表示，使用单引号，双引号，以及三个双引号都是可以的
#
# #5 占位符
# #5.1 %
# #%s 字符串通用 %d整数通用 %c单字符通用
# # name="bingbing"
# # print("名字：%s" %name)
# # age=18
# # print("名字：%s;年龄：%d" %(name,age))
# # print("%6d" %age)
# # print("%06d" %age)  # 6d表示占六位，06d表示站6位前面不足处补0
#
# #a=3.14159
# # print("%f" %a)#默认输出小数点后六位，遵循四舍五入原则
# # print("%.3f" %a  )#%.3f表示输出小数点后三位
# # print("我是%%的%%" %())
#
#
# #6 算数运算符
# #6.1 +—*/
# print(1/1)#使用算数运算符/，这个结果是个浮点数，且除数不能为0
# a=1/1
# print(type(a))#输出结果为浮点数
# #6.2 取整除  // 取商的整数部分，向下取整
# b=9//2#9/2得出的结果是浮点数就跟上面那个一样，而9//2是整数
# print(b)
# print(type(b))
# # 6.3 %取余数
# print(5%2)
# #6.4   **是取幂
# print(2**3)#输出得结果是2的3次方即8
# print(7.0//3)#使用算数运算符，若有浮点数，结果也会用浮点数表示

# #6.5 赋值运算符
# num1=5
# num2=8
# #将一个变量的值赋给另外一个变量
# num3=num1
# print(num3)
# total=num1+num2+num3
# print(total)
# #a=a+1 效果等同于a+=1
# n1=98
# n2=990
# n1+=n2  #效果就等同于n1=n1+n2
# print(n1)
#赋值运算符左右之间是不能加空格的，左右两端可以加空格
#加减乘除的使用都类似上述加法等同
#print(10+=3) #纯数字的话不能使用，赋值运算符是针对变量使用的





#7  输入函数
#input(prompt)  prompt是提示，会在控制台中显示
# input("请输入：")
# name=input("请输入名字：")#这个是每次运行程序name的值都会变
# print(name)

#8 转义字符
#8.1 \t制表符   通常表示四个字符，也称缩进
# print("sixstar")
# print("sixs\tar")#也就是说会将\t换成四个空格
# print("姓名\t年龄\t电话")#看到空格数目不是四个属于正常情况
# #8.2 \n换行符
# print()#因为print中end默认是\n即换行符
# print("haha")
# print(end="\t")
# print("haha")
#print("xixi\nhaha")
#8.3 \r 回车 表示将当前位置移到本行开头
# print("sixsta\rhuze")#作用呢就是将\r后面的部分移到本行好头，前面的部分自然就没有了
# #8.4 \\反斜杠符
# print("sixs\tar")
# print("sixs\\tar")#\\的作用呢就是将前面那个\的作用去掉
#print(r"sixs\\\\tar")#r原生字符串，默认取消转义



#9 if判断
# age=21
# if age<18:
#     print("未成年，禁止进入")
# sore=input("请输入成绩：")#input默认的是字符串类型，
# print(sore)
# if sore=='60':  #单个=是赋值 ==双等号是比较
#     print("继续加油")
# if sore=='100':
#     print("真棒，满分")
# if sore<'60':
#     print("成绩不合格")

#10 运算符
#10.1 比较运算符
# #== !=
# a=777
# b=888
# if a!=b:
#     print("二者不相等")
# print(a==b)#a==b类似这种，比较运算符都是是判断语句，输出的结果要么是bool类型
#10.2 逻辑运算符 and（与） or（或） not（非）
# a="haha"
# b="heihei"
# if a=="haha" and  b=="heihei":
#     print("a与b都满足条件")
# print(not 3>9)
#10.3  if  else  这是二选一
#基本格式
# if 条件:
#     满足条件时要做的事情
# else:    #else后面不需要添加任何东西
#    不满足条件时做的事
a =5
b =6
# print("a<=b") if a < b else print("b<a")
# 10.4 if  elif   是多选择一
# if   条件一:
#     满足条件一要做的事情
# elif  条件2：
#     满足条件二要做的事情
# elif  条件三：
#      满足条件3要做的事情
# score=input("成绩是：")
# print(type(score))
# score=int(score)#input输入的是字符串类型，需要强制类型转换为int类型才能比较数字大小
# if  60<=score<=100:
#     print("及格")
# elif 0<=score<60:
#     print("不及格")
# else:
#     print("成绩无效")
# # 10.5 if嵌套  就是if中嵌套一个if，内外层次都可以是if else 结构
# ticket=True
# temp=38.5
# if ticket==True:
#     print("有票可以进入",end=' ')#,end=" "表示不换行用空格隔开
#     if temp<38:
#         print("温度正常可以出去")
#     else:
#         print("温度太高不能出去")
# else:
#     print("没票不能进入")






