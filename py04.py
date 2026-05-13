#1.列表
#基本格式：
#列表名=[元素1，元素2，元素3......]
#所有元素放在中括号内，元素与元素之间用逗号隔开，元素之间数据类型可以不相同
#li=[1,2,"a",4]#数组下标从0开始
# print(type(li))#输出<class 'list'>就是列表类别
# print(li[0])
# #列表也可以进行切片操作
# print(li[0:3])#包前不包后
#列表也是是可迭代对象，可以for循环遍历取值
# for i in li :
#     #  print(i,end=" ")
#     print(i)#默认end=”\n“


#2.列表的常见操作
# 2.1 添加元素
# append（） extend（）insert（）
#li=["one","two","three"]
#li.append("four")#输出['one', 'two', 'three', 'four']，整体将插入对象进行添加
#print(li)
#li.extend("four")
#print(li)#输出['one', 'two', 'three', 'f', 'o', 'u', 'r']，将插入对象进行分散添加
#li.insert(1,"four")
#(li)#输出['one', 'four', 'two', 'three']，在指定位置插入新元素，原有元素往后移，一定要先指定位置，不然就报错
#li=[1,2,3]
# li.append(4)
# print(li)
# li.extend(5)#会报错，因为extend中必须是可迭代对象，而整形不是可迭代对象
# print(li)
# li.insert(3,5)
# print(li)


#2.2修改元素
#直接通过下标就可以进行修改
# li=[1,2,3]
# print(li[2])
# li[2]="a"#直接通过下标进行修改
# print(li)

#2.3 查找元素
#in：判断指定元素是否在列表中，在的话就返回true，否则就返回false
#not in:与上述相反
# li=["a","b","c"]
# li=["susu","huhu","lili"]
# while True:
#     name=input("请输入你的昵称：")
#     if name  in li:#上述可以判断输入的昵称是否在昵称列表中
#        print("名字已经存在，请换一个名字输入")
#     else :
#         li.append(name)
#         print("名字输入成功")
#         break
# print(li)

#index:返回指定数据所在位置的下标 ，如果查找的数据不存在就会报错
#count（）：统计指定数据在当前列表出现的次数
#跟字符串中的用法相同


#2.4 删除元素
#del
# li=["a","b","c","d","e","f"]
# del li
# del li[0]#删除指定位置元素
# print(li)#会报错，因为li已经被删除了

#pop：删除指定下标的数据，python3版本默认删除修后一个元素
# li=["a","b","c","d","e","f"]
# li.pop()
# print(li)#输出['a', 'b', 'c', 'd', 'e'],删除了最后一个位置元素
# li.pop(2)#删除下标为2的元素
# print(li)


#remove 根据元素的值进行删除
# li=["a","b","c","d","e","f","b"]
# li.remove("a")#删除指定元素
#li.remove("g")#因为里面没有g所以会报错
# print(li)
# li.remove("b")
# print(li)#输出['a', 'c', 'd', 'e', 'f', 'b']，默认只会删除第一次出现的元素



#3.5 排序
#sort（）：将列表按照特定顺序进行排列，默认是从小到大顺序
# li=[1,4,6,2,3,8,10]
# li.sort()
# print(li)#输出[1, 2, 3, 4, 6, 8, 10]


#reverse：倒序，就是将列表倒置过来
# li.reverse()
# print(li)#输出[10, 8, 6, 4, 3, 2, 1]，将sort排序好的进行倒序排放


#3.6 列表推导式
#格式一：[表达式 for 变量 in 列表]
#注意：in后面不仅可以放表达式，还可以放range（）,可迭代对象
# li=[1,2,3,4,5]
# [print(i,end=" ") for i in li]#前面的i是表达式，
# li=[]
# for i in range(1,5):#range内指的是取数的范围，包前不包后
#     li.append(i)
# print(li)
#更简便一点，使用列表推导式
# [li.append(i) for i in range(1,6) ]
# print(li)

#格式2：[表达式 for 变量 in 列表 if 条件 ]
#把基数放到列表里
# li=[]
# for i in range(1,11):
#     if i%2==1:
#         li.append(i)
# print(li)
# [li.append(i) for i in range(1,11) if i%2==1]
# print(li)


#3.7 列表嵌套
#含义：一个列表里面又有一个列表
# li=[1,2,3,[4,5,6]]
# print(li)#输出[1, 2, 3, [4, 5, 6]]
# print(li[2])#输出3
# print(li[3][0])#输出4
