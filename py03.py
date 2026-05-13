#1.字符串编码
#本质就是二进制数据与语言文字一一对应的关系
#Unicode：所有字符都是2个字节，与数字转换速度比较快
#utf-8 对不同的字符使用不同的长度表示，节省空间，字符与数字（二进制的0和1）转换速度比较慢
from dataclasses import replace
from tkinter.font import names

# #2.字符串编码转换
# a="hello"
# print(a,type(a))#str类型（字符串类型），字符串是以字符形式进行处理
# a1=a.encode()#编码
# print(a1)
# print(type(a1))#bytes，已经不是字符串类型了，变成了以字节为单位进行处理的
# a2=a1.decode()#解码
# print(a2)
# print(type(a2))
#
# st="你好"
# st1=st.encode("utf-8")
# print(st1)
# print(st1,type(st1))
# st2=st1.decode("utf-8")
# print(st2)
#这个encode和decode默认是编码和解码形式是unicode形式，若括号中写了固定的编码方式则编码和解码就按照这个形式来

#3.字符串常见操作
#3.1 +字符串拼接
# print(10+10)#输出为20，整形相加，这里的加号是算数运算符
# print("10"+"10")#输出为1010，字符串相加，+是字符串拼接
# name1="你"
# name2="好"
# name3="呀"
# print(name1+name2)
# print(name1,name2,name3,sep="")#","是分隔输出变量的，sep是定义多输出变量间用什么隔开，默认是sep=” “，即一个空格隔开
#
# #3.2 *在字符串中是重复输出
# print("好好学习，天天向上"*3,sep="\n")#这个是错误的，因为会先执行输出三遍在换行，导致输出的三遍之间还是连续的
# print("好好学习，天天向上\n"*3)
#print("$\t"*3)

#3.2 成员运算符
#作用：检查某个字符串中是否包含某个子字符串（即某个字符或多个字符）
# in:如果包含的话返回true，不包含的话返回flase
# not in：不包含的话返回true，包含的话返回false
# name="bingbing"
# print("bing" in name)  #true
# print("a" in name)     #false
# print("bing"not in name)
# print("a" not in name)
# name='冰冰'
# print("冰" in name)#中英文都适用


#3.3 下标
#python中下标从0开始
#作用：通过下标快速找到对应的数据
#格式：字符串名[下标]
# name='sixe'
# print(name[1])#输出i，因为下标从0开始
# #print(name[4])#报错，取值的时候不要超出下标范围
# #从右往左数，下标从-1开始，-1，-2，-3等
# print(name[-1])#输出的就是最后一个字符

#3.4切片
#含义：指对操作的对象截取其中一部分的操作
#语法：[开始位置:结束位置:步长]
#遵循包前不包后原则（不包含结束位本身）
# st="abcdefg"
# print(st[0:4:1])#abcd步长默认是1
# print(st[0:])#abcdefg从某个位置开始一直到结束的话，只需写起位置就好了，下标0之后的全部截取到
# print(st[:5])#abcde，下标5之前的全部截取到，不包含5
# print(st[-1:])#g，默认是从左往右切的，-
# print(st[-1:-5])#什么也没输出
# #步长的绝对值大小决定切取的间隔，正负号决定切取方向,正数表示从左往右，负数表示从右往左
# #所以想要从后往前输出的话就需要step=-1
# print(st[-1::-1 ])
# print(st[-1:-5:-1])


#4.字符串常见操作
#4.1.1查找 find
#findL:检查某一个子字符串是否包含在字符串中，如果在就返回这个子字符串开始位置的下标，否在返回-1
#find(子字符串，开始位置下标，结束位置下标）
#开始位置和结束位置下标可以省略，表示在整个字符串中查找
# name="finsdf"
# print(name.find("fin"))#返回0，返回的是查找到字符串的起始下标
# name1="bingbing"
# print(name1.find("bing",3))#这个3是查找的起始位置，指的是从该下标开始查起
#
# print(name1.find("b",3,5))#返回4，这里面3是起始位置，5是结束位置
# #包前不包后
# print(name1.find("b",3,4))#输出-1

#4.1.2 index() 与find一样，找到的话返回下标，
#index(要查找的字符串，起始位置下标，结束位置下标）
# name="bingbing"
# print(name.index("bing"))#输出0
# print(name.index("binge"))#会报错,之后的代码不再执行
# #同样遵循包前不包后原则

#4.1.3 count（）：返回某个子字符串在整个字符串中出现的次数，没有就返回0
# name="bingbing"
# print(name.count("b"))#输出2，同样可省略起始和结束位置下标，遵循包前不包后原则
# print(name.count("a"))#输出0，没有出现过
# print(name.count("b",1))#输出1，因为从下标1，即第二个元素开始查找的

#4.2判断
#4.2.1 startswith（）：判断是否已某个字符串开头，是的话返回true，否则返回false，如果设置指定开始和结束位置，则在指定范围内检查
#startswith("子字符串",起始位置，结束位置)
# name="bingbing"
# print(name.startswith("bing",0))#输出true
# print(name.startswith("g",3))#输出true

#4.2.2 endswith（）：判断是否以某个字符串结尾，是的话返回true，否则返回false
#语法类型与上述的相同，都遵循抱歉不包后原则
# name="bingbing"
# print(name.endswith("bing"))#返回true

#4.2.3 isupper():检测整个字符串中是否都是大写，是的话返回true，；否则返回false
# name="bingbing"
# print(name.isupper())#返回false
# print("SID".isupper())#返回true


#4.3 修改元素
#1.replace（）：替换
#语法，replace（旧内容，新内容，替换次数）
# name="好好学习,天天向上"
# print(name.replace("天","时"))#好好学习,时时向上 ，不写替换次数就默认全部替换
# print(name.replace("天","时",1))#输出好好学习,时天向上，替换次数设为1，就只替换一次
#
# #2.split（）：指定分隔符来分字符串
# st=("hello,python")
# print(st.split(","))#输出['hello', 'python']，以列表的形式返回
# #如果字符串中不包含分割内容，就不进行分割，作为一个整体
# print(st.split("a"))#['hello,python'],里面没有a，不进行分割，原样输出
# print(st.split("o"))#输出['hell', ',pyth', 'n']，就是将分隔符替换分割界限
# print(st.split("o",1))#['hell', ',python']分割次数设为一，那么就将第一个出现分割符的地方进行分割，若不定义分割次数，那么就将所有出现分隔符的地方进行分割
#
#
#
# #3.capitalize():第一个字母大写
#
# st="bingbing"
# print(st.capitalize())#输出Bingbing


#4.lower（）：大写字母转为小写
# st="BinG"
# print(st.lower())#输出bing，将所有大写都转换为了小心


#5.upper（）：小写字母转为大写
# st="bing"
# print(st.upper())#输出BING,将所有小写字母转为大写















