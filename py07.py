#1.类型转换
#float-》int
# a=1.3
# print(a,type(a))
# b=int(a)
# print(b,type(b))
# print(int(1.9))
#浮点型强转整形会去掉小数点及后面的数，只保留整数部分
#str->int
# print(int("123"))#字符串类型转整形字符串必须是纯数字
# print(int("bingbing"))#会报错
#如果字符串中有数字和正负号以外的字符就会报错
# print(int("-100"))#输出-100
#+/-写在前面表示正负号，不可以写在后面
# print(int("29-80"))#会报错

#用户从控制台输出，判断年龄
# age=int(input("请输入年龄："))#input默认输入的是字符串类型
# if age>=18:
#     print("成年了")




#1.2 float(）：转换为一个小数
# print(float(11))#输出11.0，整型转换为浮点型会自动添加一个小数
# print(float(-10))#输出-10.0
# print(float("-13.34553"))#输出-13.34553
#用法与int一样



#1.3 str():字符串类型 ，任何类型都可以转化为字符串类型
# n=100
# print(type(n))
# n1=str(n)
# print(type(n1))#输出<class 'str'>
# st=str(-1.20)
# print(st,type(st))#-1.2 <class 'str'>
# n2=str(1.0000000)
# print(n2,type(n2))#1.0 <class 'str'>
#float型转换为str会去除末尾为0的小数部分
# st=str([1,3,4,5])#列表可以转换成字符串类型
# print(st,type(st))




#1.4 eval（）：用来执行一个字符串表达式，并返回表达式的值
# print(10+10)#输出20
# print("10"+"10")#1010
# print("10+10")#10+10
# print(eval("10+10"))#输出20，执行运算并返回运算的值

#eval（）可以实现list，dict，tuple和str之间的转换
# #str-》list
# st1="[[1,2],[3,4]]"
# print(type(st1))#<class 'str'>
# li=eval(st1)
# print(li,type(li))#[[1, 2], [3, 4]] <class 'list'>


#str->dict
#st2="{"name":"bingbing","age":20}"#这句会报错，双引号中不能出现未转义的双引号，不然会认为结束
# st2="{'name':'bingbing','age':20}"
# dic=eval(st2)
# print(dic,type(dic))#{'name': 'bingbing', 'age': 20} <class 'dict'>


#eval（）非常强大，但是不够安全，容易被恶意修改数据，不建议使用
#1.5 liat（）：将可迭代对象转换成list
#支持转换为list的类型：str，tuple，dict，set
#1.str-》list
#print(list("abcdefg"))#输出['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(list(12345))#会报错，因为整形不是可迭代对象

#tuple->list 元组转化为列表
# print(list((1,2,3,4,5)))#[1, 2, 3, 4, 5]

#dict-》list
# print(list({"name":"binging","age":20}))#输出['name', 'age']，字典转化为列表，会取键名作为列表的值

#set-》list 集合转化为列表
# print(list({1,2,3,4,5}))#输出[1, 2, 3, 4, 5]
# print(list({"a","b","c"}))#输出['b', 'a', 'c']，集合是无序的
#集合转化成列表会先去重，再转化成列表












