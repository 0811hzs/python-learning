#1.while循环
# 1.1基本语法
# 定义初始变量
# while 变量：
#     循环体
#     改变变量
# i=10
# while i>0:
#     print("好好学习，天天向上")
#     i-=1
# 1.2 while True :#条件为True，一直为真，就会一直执行
#          循环结构
# 上述就是死循环
# while "haha":#只要条件不是False或0，其他单独存在的值也会是死循环
#     print("永远18岁")
#
# i=1
# j=0
# while i<=100:
#     j=j+i
#     i+=1
# print(j)

#2.while循环嵌套（含义：一个while循环里面还有一个while循环）
# while 条件1：
#     循环体1
#     while 条件2：
#         循环体2
#         改变变量2
#     改变变量1
# 注意：缩进决定层级，严格控制缩进，最好自动缩进
# i=1
# while i<=3:
#     print(f"循环次数是{i}")
#     j=1 #记录内循环次数
#     while j<=5:
#         print(f"内循环次数{j}")
#         j+=1
#     i+=1


#3.for循环
# for 临时变量 in 可迭代对象：
#     循环体
#str="helloworld"#定义一个字符串
# #一般用于一个一个的取值，上述str就是迭代对象，可迭代对象就是要遍历取值的整体
# for i in str:#i是临时变量可随便写，i是常规写法
#     print(i)
# 若上述str=1234就会报错，因为int类型不是可迭代对象
#可以将1234加引号,使其变为字符串类型

#3.2 range()
#用来记录循环次数,相当于计数器
#range(start,stop,step) 里面有三个参数
# for i in range(1,6):#从1开始到5结束,遵循包前不包后原则
#     print(i)
# for i in range(5):#输出结果是从0到4
#     print(i)
#包前不包后,包含开始位置的数字,不包含结束位置的数字
# #range()里面只有一个数字,这个数字就是循环的次数,默认从0开始
# str="hello"
# for i in str:
#     print("你好")

# total=0
# for i in range(1,101):
#     total+=i
# print(total)
# i=0
# while i<=100:
#     total+=i
#     i+=1
# print(total,end=" ")
# print("输出结果:",total)


#4.
# break 中途退出,结束循环
# countinue 结束当前循环,进入下一循环
#二者都是在循环中使用的关键子
# i=1
# while i<10:
#     print("我在吃苹果")
#     break


# i=1
# while i<3:
#     print(f"在吃第{i}个苹果")
#     if i==2:
#         print("吃饱了,不吃了")
#         break
#     i+=1
# j=1
# while j<8 :
#     print(f"在吃第{j}个苹果")
#     if j==4:
#         print(f"第{j}个苹果有虫子,这个不吃了")
#         continue#continue的作用是自动跳过本次循环中余下的代码，直接回到循环的开始进行下一次的迭代，所以目前代码会进入死循环，解局之法是在continue前加入j+=1
#     j+=1





