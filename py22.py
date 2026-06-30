#协程:是python中另外一种实现多任务的方式，只不过比线程更小，占用更小执行单元(也就是需要的资源).他自带cpu上下文
#这样只要在合适的时机，我们可以把一个协程切换到另一个协程，只要这个过程中保存或回复cpu上下文哪个程序还是可以运行的
#其实就是单线程下的开发，又成为微线程
#注意:线程和进程的操作是由程序触发系统接口，最后的执行者是系统，而协程的执行者是程序员，什么时间来切换由程序员自己来决定
#1.1简单实现协程
from ctypes.wintypes import HTASK

#
# def test1():
#     yield "a"
#     yield "b"
#     yield "c"
#     yield "d"
# def test2():
#     yield "b"
#     yield "c"
#     yield "d"
# if __name__=="__main__":
#   t1=test1()
#   print(t1)
#   t2=test2()
#   print(t2)
#<generator object test1 at 0x00000294F9A4B580>
#上述二者都是生成器对象generator ，有了yield这个关键字就是生成器对象
  # print(next(t1))
  # print(next(t1))
  # print(next(t1))
  # print(next(t2))
#1,2应用场景
#如果一个线程中io操作比较多的时候可以用协程
#适合高并发处理
#2.greenlet：是一个由c语言实现的协程模块，通过使用switch来实现任意函数之间的切换
#安装第三方模块
#2.1 安装  pip install greenlet/模块名
#卸载: pip uninstall greenlet/模块名
#查看已安装的模块:pip list
#2.2主要greenlet属于手动切换，当遇到io操作程序会阻塞而不能自行切换
#2.3通过greenlet实现任务的切换
#导入greenlet模块
# from greenlet import greenlet
# def sing():
#     print("在唱歌")
#     t2.switch()#跳到dance
#     print("唱完歌了")
# def dance():
#     print("在跳舞")
#     print("跳完舞蹈了")
#     t1.switch()#跳回sing
# if __name__ == "__main__":
#     #创建协程对象：greenlet(任务名)
#     t1=greenlet(sing)
#     t2=greenlet(dance)
#     #t1.switch()#切换到t1中去运行
#     t2.switch()#
#3，gevent:遇到io操作时，会进行自动切换，属于主动式切换
#3.1使用:
import  gevent#导入gevent模块
#gevent.spawn（函数名）:创建协程对象
#gevent.sleep（）:耗时操作
#gevent.join（）:阻塞，等待某个协程执行完毕
#gevent.joinall():等待所有协程对象都结束在退出，参数是一个协程对象列表
# def sing():
#     print("在唱歌")
#     gevent.sleep(3)
#     print("唱完歌了")
#
# def dance():
#     print("在跳舞")
#     print("跳完舞了")
# if __name__ == '__main__':
#     #创建协程对象
#     g1=gevent.spawn(sing)
#     g2=gevent.spawn(dance)
#     #阻塞，等待协程执行结束
    #g1.join()#join才是让其工作的地方，并等待g1对象执行结束
    #g2.join()
#3.3joinall():
import  time
# def sing(name):
#     for i in  range(3):
#         gevent.sleep(1)#只有使用这个才能自动任务切换，写成time，sleepp(1)是不会自动任务切换的
#         print(f"{name}在唱歌，第{i}遍了")
# if __name__=="__main__":
#     gevent.joinall([
#         gevent.spawn(sing,"bingbing"),
#         gevent.spawn(sing," lihua")
#                     ])
#joinall():等待所有的协程对象都执行完再退出
#3.4 monkey补丁:拥有在模块运行时替换的功能
#导入模块:
# from gevent import  monkey
# monkey.patch_all()#将用到的time.sleep()代码替换成gevent里面自己实现耗时操作的gevent.sleep（）代码
# #注意:monkey.patch_all()这句话一定要放在被打补丁的前面
# def sing(name):
#     for i in  range(3):
#         time.sleep(1)#只有使用这个才能自动任务切换，写成time，sleepp(1)是不会自动任务切换的
#         print(f"{name}在唱歌，第{i}遍了")
# if __name__=="__main__":
#     gevent.joinall([
#         gevent.spawn(sing,"bingbing"),
#         gevent.spawn(sing," lihua")
#                     ])
#4.总结:
#4.1 线程是cpu的基本单位，进程是资源分配的基本单位，
#4.2 进程，线程和协程对比
#    进程:切换需要的资源最大，效率最低
#    线程:线程谢欢需要的资源一般，效率一般
#    协程:协程切换需要的资源最小，而且效率高
#多线程适合io密集型操作（文件操作，爬虫），多进程适合cpu密集型(科学计算，对视频进行高清解码)
#进程，线程和协程都是可以完成多任务的， 可以根据自己实际开发的需要进行选择





















