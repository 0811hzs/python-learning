#1.正则表达式
#字符串处理工具
#注意需要导入re模块
import re
from idlelib.debugger_r import restart_subprocess_debugger

#1.2特点:
#       语法比较复杂，可读性较差
#       通用性很强，适用于多种编程语言
#1.3 步骤:
# 1.导入re模块
# 2.使用match（）方法进行匹配操作，re.match()方法能匹配出以xxx开头的字符串，如果其实位置没有匹配成功，就返回None
#re.match(pattern,string)
#pattern：匹配的正则表达式
#string：要匹配的字符串
# r=re.match("泽","泽省开路虎")#如果匹配到了r就是一个match对象，要是没匹配到就返回None
# print(r)#<re.Match object; span=(0, 1), match='泽'>
# #如果上一步数据匹配成功，使用group()提取数据
# print(r.group())
#注意:match是从开始位置匹配，匹配不到就没有就返回None，并且无法group，且匹配的是表达式整体

#二.匹配单个字符
#1."."匹配任意一个字符除/n以外  ---常用
# res=re.match("..","hello")#匹配一个字符就加一个.匹配两个就两个..
# print(res)
#2.[]匹配[]中列举的字符  --常用
# res=re.match("[he]","ello")#[]是匹配一个字符，只要[]中有一个字符跟string中开头的字符对应，那就是匹配成功了，就会输出哪个
# print(res)
#匹配0到9的两种写法:
#方法一：
# res=re.match("[0123456789]","9876")
# #第二种方法:
# res2=re.match("[0-5-9]","987654321")
# print(res)
# print(res2)
# res3=re.match("[a-zA-Z]","Hello87654321")#a-zA-Z表示列举出所有大小写字母
#3.\d 表示匹配数字0-9    --常用
# re=re.match(r"\d\d","78698")#在前面加一个r这样就会把\当成普通字符了
# print(re)
# print(re.group())
#4,\D:匹配非数字    --常用
# res=re.match(r"\D","r343")
# print(res)
# print(res.group()) #r
#5,\s：匹配空白，即空格和table键
# res=re.match(r"\s\s","  hdfhsdhkfsd")#一个tab键相当于2个空格
# print(res)
# print(res.group())
#6.\S :匹配非空白
# res=re.match(r"\S","hhlhol")
# print(res)
# print(res.group())
# #7.\w:匹配单词字符,即a-zA-Z，0-9，_,汉字   --常用
# res=re.match(r"\w","_080990")
# print(res)
# print(res.group())
#8.\W：匹配非单词字符
# res=re.match(r"\W",".djfjdf")
# print(res.group())
#总结:上述都是匹配单个字符


#三.匹配多个字符:
#1.*匹配前一个字符出现0次或无限次，即可有可无  --常用
#2.+匹配前一个字符出现一次或无限次，即至少一次   --常用
#3.？匹配前一个字符出现一次或零次             --常用
#4.{m}匹配前一个字符出现m次
#5.{m,n}匹配前一个字符出现最少m次最多n次
# res=re.match(r"\w*",".6676878.jdif")
# print(res.group())#6676878
# res=re.match(r"\w+","6676878.jdif")
# print(res.group())
# res=re.match(r"\w?","6676878.jdif")
# print(res.group())
# res=re.match(r"\w{3}","78f0hhde")
# print(res.group())
# res=re.match(r"\w{3,3}","87967867")
# print(res.group())

#四.匹配开头和结尾
#1。^：匹配字符串开头；表示多……取反
# res=re.match("^py","python")
# print(res.group())#此时表示以……开头
#注意：^在[]中表示不匹配
# res=re.match("[^py]","thon")#这句话的意思是匹配一个既不是p也不是y的开头
# print(res.group())#输出t
#2.$匹配字符串结尾
# res=re.match(".*g$","bingnbing")#匹配一个以字母 g 结尾的字符串，并且会贪婪地匹配从开头到最后一个 g 之间的所有内容。
# print(res.group())






