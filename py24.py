#导入模块
import re
#一.匹配分组
#1.|匹配左右任意一个表达式    --常用
# res=re.match("abc|def","abc")
# print(res.group())#abc

#2.（ab）将括号中字符当作一个分组  --常用
# res=re.match(r"\w*@(163|qq|126).com","123@qq.com")
# print(res.group())

#3.\num 匹配分组num匹配到的字符串    --经常被匹配标签时被使用
# res=re.match(r"<\w*>\w*<\w*>","<html>login<html>")
# print(res.group())


