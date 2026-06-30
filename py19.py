#线程
#1.1线程之间共享资源（全局变量)
from  threading import Thread #导入线程模块 thread是线程的意思  #这个方式是调用其中的部分函数
# import  time#该模块提供与时间相关的各种函数#这个是调用这个模块
# li=[]
# def wdata():
#     for i in range(5):
#         li.append(i)
#         time.sleep(1)#程序会在这里暂停1s
    #return "写入的数据:",li
# def rdata():
#     print(li)
# if __name__ == '__main__':#通过使用这种方式，别人在调用本模块的时候是看不到下面的代码的
    #创建子线程
    # t1 = Thread(target=wdata)  # 创建第1个线程，分配的任务是执行 wdata 函数
    # t2 = Thread(target=rdata)  # 创建第2个线程，分配的任务是执行 rdata 函数
    #使用Thread函数是创建一个子线程，target是Thread函数中的关键参数，用来指明函数运行后执行的函数名称
    #开启子线程
    # t1.start()# 这句话的意思就是通知t1和t2进程开始干活
    # #t1.join()#join函数的意思是等上述 t1.start()执行完了在往下接着执行
    # time.sleep(1) #很多时候不使用join()函数，使用time的sleep函数也可以达到预期的效果，重点是暂停的时间需要合适
    # t2.start()# 这句话的意思就是通知t1和t2进程开始干活
    # t2.join()
    #多个子线程是同时运行的，有的执行的快，有的执行的慢，为了达到预期的效果，很多时候join()方法是有必要使用的

#1.2 资源竞争
# a=0
# b=1000000
# def add():
#     global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
#     for i in range(b):
#         a+=1
#     print("第一次结果:",a)
# # add()
# def add2():
#     global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
#     for i in range(b):
#         a+=1
#     print("第二次运行结果:",a)
# # add()
# # add2()
# if __name__=="__main__":
#  t1=Thread(target=add)
#  t2=Thread(target=add2)
#  t1.start()
#  t1.join()
#  t2.start()
#因为对全局变量a没加锁，存在多个函数同时对同一个全局变量进行操作的可能，就是同时对同一变量进行修改等

#线程同步
#2.1两种方式：线程等待（join）和互斥锁
# a=0
# b=1000000
# def add():
#     global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
#     for i in range(b):
#         a+=1
#     print("第一次结果:",a)
# # add()
# def add2():
#     global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
#     for i in range(b):
#         a+=1
#     print("第二次运行结果:",a)
# # add()
# # add2()
# if __name__=="__main__":
#  t1=Thread(target=add)
#  t2=Thread(target=add2)
#  t1.start()
#  t1.join()
#  t2.start()
#互斥锁:对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题，保证同一时刻只能有一个线程去执行
#方法：acquire():上锁
#release():释放锁
#必须成对存在,否则容易产生死锁
from threading import Lock#用于创建互斥锁
a=0
b=1000000
lock=Lock()#创建一个互斥锁对象
def add():
    lock.acquire()#上锁
    global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
    for i in range(b):
        a+=1
    print("第一次结果:",a)
    lock.release()#解锁
# add()
def add2():
    lock.acquire()#
    global a#就是只要再函数内部对变量进行数值上的改变那么就是局部变量，但a还没有初始化所以显示错误，解决方式是通过global使其为全局变量
    for i in range(b):
        a+=1
    print("第二次运行结果:",a)
    lock.release()
# add()
# add2()
if __name__=="__main__":
 t1=Thread(target=add)
 t2=Thread(target=add2)
 t1.start()
 t2.start()
#注意：互斥锁是全局变量，是多个进行一起去抢，抢到锁的进程先执行。
#这互斥锁还好存在问题的，他只能保证同一时间段只有一个函数操作某个对象，但是不能保证操作顺序



