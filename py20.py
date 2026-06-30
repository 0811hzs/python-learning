#进程:是操作系统进行资源分配和资源调度的基本单位，是操作系统结构的基础
#一个正在运行的程序或者软件就是一个进程
#程序跑起来就成了进程
#注意：进程里面可以创建多个线程，多线程可以完成多任务
#1.2进程的状态
#1.就绪状态：运行的条件都已经满足，正在等待cpu执行
#2.执行态：cpu正在执行其功能
#3.等待（阻塞）状态：等待某些条件满足，如一个程序sleep了，此时就处于等待状态
# import time
# print("我是泽省")#程序开始，处于执行状态
# a=input("请输入年龄：")#等待输入年龄，处于阻塞态
# print(a)#处于执行状态，因为已经等到a了，条件已经够了
# time.sleep(1)#延迟1s，处于阻塞态
import queue
from concurrent.interpreters import Queue
#进程语法结构
# multiprocessing模块提供了Process类代表进程对象
#2.1 Process 类参数
#1.target：执行的目标任务名，即子进程要执行的任务
#2，args:以元组()的形式传参，用来表示可变数量的位置参数
#3.kwargs:以字典{}形式传参
#[]这种的是列表形式
#2.2 方法
#1.start():开启子进程（子进程就是父进程在执行过程中又产生了一个新的进程，这个进程跟原进程不共享空间）
#is_alive()：用于判断子进程是否还活着，存活返回True，否则返回False
#3.join():主进程等待子进程执行结束
#2.3 常用的属性
#name：当前进程的别名，默认是Process—N，这个N是递增的一个整数
#pid:当前进程的进程编号
#导入模块
from multiprocessing import Process#导入进程模块
import os
import time
from platform import processor


# def sing():
#     #os.getpid（）：
#     # 获取当前进程编号
#     print("主进程的pid:",os.getppid())#也就是当前子进程的父进程的进程号，也就是当前主进程的pid
#     #print(f"sing子进程编号:",os.getpid())
#     print("唱歌")
# def dance():
#     #print(f"dance子进程编号:", os.getpid())#在定义方法的时候使用的是os.getpid()以及os.getppid(),在定义好子进程之后再输出pid的话，
#     # 直接使用进程对象.pid和os,pid()可以了
#     print("跳舞")
# if __name__=="__main__":#在使用 multiprocessing 模块创建子进程时，if __name__ == "__main__": 这一句是必须有的
#     #创建子进程
#     #修改子进程名字
#     t1 = Process(target=sing,name="子进程1")
#     t2 = Process(target=dance,name="子进程2")
#     t1.start()
#     t2.start()
#     #第二种修改方式：
#     t1.name="子进程一"
#     t2.name="子进程二"
#     #访问name属性
#     print(t1.name)#Process-1，子进程1
#     print(t2.name)#Process-2，子进程2
# #就是执行到t1和t2.start的时候就开启了子进程马，之后执行print函数，与子进程是并行执行的，但执行的比子进程快所以就先输出
#    #查看子进程的进程编号
#     print(t1.pid)
#     print(t2.pid)
#     print(os.getpid())#这个输出的是当前主进程的pid
#     #time.sleep(5)
#     print("pycharm的pid:",os.getppid())#这个输出的是当前主进程的父进程的pid也会是pycharm这个app的pid

# def eat(name):
#     print(f"{name}在吃饭")
# def sleep(name):
#     print(f"{name}在睡觉")
# if __name__ == "__main__":
#     p1=Process(target=eat,args=("泽省1",),name="p1子进程")#输入的元组当只有一个输入的时候后面必须加,
#     p2=Process(target=sleep,args=("泽省2",),name="p2子进程")#在创建进程时Process的P需要大写
#     p1.start()
#     p1.join()#主进程处于等待的状态，p1处于运行的状态
#     p2.start()
#     print("p1的存活状态:",p1.is_alive())#p1的存活状态: False,因为p1已经执行结束了，所以进程就没了，所以是失活状态

# 2.4进程间不共享全局变量
# li=[]
# def wdata():
#     for i in range(5):
#         li.append(i)
#         #time.sleep(1)#程序会在这里暂停1s
#     print("写入的数据:",li)
# def rdata():
#     print("读出的数据:",li)
# if __name__ == '__main__':#1.防止别人导入文件的时候执行main里面的方法
#                           #2.防止windows系统递归创建子进程
# #元组是（），列表是[]
#    p1=Process(target=wdata,name="子进程一")
#    p2=Process(target=rdata,name="子进程二")
#    p1.start()#写入的数据: [0, 1, 2, 3, 4]
#    p1.join()
#    p2.start()#读出的数据: []
   #进程不共享全局变量，所以写入是写入了，但读取还是为空
   #想破局的话就不用进程，换用线程来解题

#3 进程间的通信
#Queue(队列)
# q.put():放入数据
# q.get():取出数据
# q.Empty():判断队列是否为空
# q.qszie():返回当前队列包含的消息数量
# q.full():判断队列是否满了
from queue import Queue#导入Queue
#初始化一个队列对象
# q = Queue(3) #最多可接受三条消息，没写或者是负值就代表没有上限，直到内存的尽头
# q.put("生来平困不怕苦")
# q.put("双全打出大路虎")
# print(q.qsize())
# print(q.get())#获取队列中的一条消息，然后将其从队列中移除
# print(q.get())
# print(q.empty())
# print(q.full())
# print(q.qsize())

from queue import Queue
from multiprocessing import Queue
li=["张三","lisi"]
def wdata(q1):
    for i in range(5):
        print(f"{i}已经被放入")
        q1.put(i)
        #time.sleep(1)#程序会在这里暂停1s
        # 生产完毕后，放入一个结束信号（哨兵值 None）
    q1.put(None)
def rdata(q2):
    while True:
        #判断队列是否为空，队列为空就退出循环
       item=q2.get()
       if item is None:
            break
       else:
         print(item)

if __name__ == '__main__':#1.防止别人导入文件的时候执行main里面的方法
                          #2.防止windows系统递归创建子进程
#元组是（），列表是[]
   # 创建队列对象，也就是实例化一个对象
    q=Queue()
    p1=Process(target=wdata,args=(q,))
    p2=Process(target=rdata,args=(q,))
    p1.start()#写入的数据: [0, 1, 2, 3, 4]
    p1.join()
    p2.start()




