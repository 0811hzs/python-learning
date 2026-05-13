#1，元组
#1.1基本格式：元组名=（元素1，元素2，元素3......)
#所有的元素都包含在小括号内，个元素直接用逗号隔开，各元素可以属于不同的数据类型
# tua=(1,2,3,4,"a")
# print(type(tua))#输出<class 'tuple'>，为元组类型
# tub=(1)
# print(type(tub))#输出为int型
# tuc=(1,)
# print(type(tuc))#输出为<class 'tuple'>，只有一个元素时末尾必须加上",",否则返回这个唯一值的数据类型
# tud=()#这是定义的空元组
# print(type(tud))#输出<class 'tuple'>

#1.2元组与列表的区别 ：
#1.元组只有一个元素的时候后买你需要加逗号，列表就不需要
#2.元组只支持查询操作，不支持增删改操作
#li=[1,2,3,1]
# li[2]=0
# print(li)#[1, 2, 0]
# li1=(1,2,3)
# print(li1[2])#输出3，元组也有下标，也是从0开始，从左往右,
# print(li1[-1])#输出3，最后一个元素下标为-1，从右往左，依次为-1，-2，-3，-4
#li1[2]="a" #会报错，因为元组不支持更改，只支持查询
#count(),index(),len()这些函数的用法在元组中与列表中相同
# print(li.index(2))#输出1，index定义的是括号中元素在列表/元组中首次出现的位置
# print(li.count(1))#输出2，count（）函数是统计括号中的元素共出现过几次的
#print(len(li))#输出4 len是确定列表/元组的长度
#print(li[1:3])#输出[2, 3]，这是进行的切片操作，[]中的数字是下标，遵循包前不包后

#1.3 应用场景
#函数的参数和返回值
#格式化输出后面的（）本质上就是一个元组
# name ="bingbing"
# age=18
# print("%s的年龄是：%d" %(name,age))#（name，age）本质上就是一个元组
# info =(name,age)
# print(type(info))#输出<class 'tuple'>，就是元组类型
# print("%s的年龄是:%d" %info)
#1.3.2 数据不可以被修改，保护数据安全{


# 2.字典
# 2.1 基本格式： 字典名={键名1：值1，键名2，值2}
# 键值对形式保存：键名和值之间用：隔开，每个键值对之间用逗号隔开
#dic = {"name": "bingbing", "age": 20}
#print(type(dic))  # 输出<class 'dict'>,dict是字典类型
# 字典中的键具有唯一性，但是值可以重复
# dic2 ={"name":"bingbig","name":"susu"}
# print(dic2)#输出{'name': 'susu'}，虽然有两个name不会报错，但是后面的name值会前面的name值覆盖
# print(dic)#输出{'name': 'bingbing', 'age': 20}


#2.2 字典的常见操作一
#2.2.1 查找元素
# 变量名[键名]
# dic={"name":"bingbing","age":39}
# #print((dic[1]))#会报错，不可以根据下标查找，字典中没有下标，查找元素需要根据键名，键名相当于下标
# print(dic["name"])#输出bingbing
# print(dic["sic"])#会报错，因为键名不存在
#变量名.get(键名)
# dic={"name":"bingbing","age":39}
# print(dic.get("name"))#输出bingbing
# print(dic.get("tel"))#键名不存在的时候不会报错，会返回none
# print(dic.get("tel","不存在"))#输出”不存在“，后面那个是当键名不存在时的返回值，默认是None

#2.2.2 修改元素
# dic={"name":"bingbing","age":39}
# dic["age"]=20 #将dic的age的值改为20，列表通过下标修改，字典通过键名更改
# print(dic)

#2.2.3 添加元素
# dic["tel"]=1234453#键名存在就修改，不存在就新增
# print(dic)

#2.2.4 删除元素
#del
#删除整个字典， del+字典名
# dic={"name":"bingbing","age":39}
# print(dic)
# del dic
# print(dic)#报错，显示dic未被定义，说明dic删除成功

#2.2.5 删除指定的键值对，键名不存在就会报错
# dic={"name":"bingbing","age":39}
# del dic["name"]
# print(dic)#输出{'age': 39}，删除成功
# # del dic["tell"]#会报错，显示tell该键不存在
# print(dic)


#2.2.6 clear（） ：清空整个字典里面的东西，但保留了这个字典
# dic={"name":"bingbing","age":39}
# dic.clear()
# dic["age"]=100
# print(dic)#输出{'age': 100}d

#pop():删除指定键值对，键不存在的时候会报错
# dic.pop("age")
#若删除的键名不存在会报错
# print(dic)#输出{}
#dic.pop()#括号中不可以什么都不写
#dic.popitem() #默认删除最会一个键值对信息

#字典常见操作二
#1.len()求长度
# dic={"name":"bingbing","age":18}
# print(len(dic))#输出2 ，说明有两个键值对


# #2.keys():返回字典中包含的所有键名
# print(dic.keys())#输出dict_keys(['name', 'age'])
# for i in dic.keys():#只取出键名
#     print(i)



#3.values():返回字典里面包含的所有值
# dic={"name":"bingbing","age":18}
# print(dic.values())#输出dict_values(['bingbing', 18])
# for i in dic.values():
#     print(i)#输出bingbing   18

#4.items（）：返回字典里面包含的所有键值对，键值对以元组形式
# dic={"name":"bingbing","age":18}
# print(dic.items())#输出dict_items([('name', 'bingbing'), ('age', 18)])
# for i in dic.items():
#     print(i)#('name', 'bingbing')#('age', 18)
#     print(type(i))


#字典的应用场景
#使用键值对，存储描述一个物体的相关信息
