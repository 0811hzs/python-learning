 #文件的读写
 #1.文件就是存储在某种长期存储设备上的一段数据
 #1.2 文件操作：打开关闭文件，读写操作
 #1.3文件对象的方法
 #1.open():创建一个file对象，默认是以只读方式打开的
 #2.read(n):n表示从文件中读取的数据的长度，没有传n就表示默认读取所有内容
 #3.write():将指定内容写入文件
 #4.close():关闭文件
 #1.4  属性
 #1.文件名.name:返回要打开文件的文件名，可以包含文件的具体路径
 #2.文件名.mode:返回文件的访问模式
 #文件名.closed:检查文件是否关闭，关闭就返货True
 #打开文件：
# f=open("test.txt")#open返回一个文件对象，对文件的所有操作都通过他
# print(f.name)#返回文件的文件名
# print(f.mode)#返回文件的访问模式输出r--只读模式
# print(f.closed)#返回文件是否已经关闭
# #关闭文件
# f.close()
# print(f.closed)#输出True

#2.读写操作
#2.1read(n):n表示从文件中读取的数据的长度，没有传n或n传入的是负值就表示默认读取所有内容
#2.1read(n):n表示从文件中读取的数据的长度，没有传n或n传入的是负值就表示默认读取所有内print(f.read(5))#就会输出前5个字符
# f=open(r"D:\Desktop\test.txt")#这个默认读取的是本文件夹下的文件，若想读取其他文件夹里的文件需要写具体路径
# print(f.read(5))#就会输出前5个字符
# print(f.read(10))#这是最多读取10个数据，第二次读取是在第一次读取的基础上接着读取的
# print(f.name)#会输出文件所在的具体路径（绝对路径）
# f.close()
#2.2readline():
# # print(f.readline())
# # print(f.readline())
# #比如想要一行一行的全部读取可以使用循环
# while True:
#    text=f.readline()
#    if not text:
#     break
#    print(text)
# for i in f:
#     text=f.readline()
#     if not text:#用于判断是不是读到了文件末尾
#      break
#     print(text)
# f.close()
#2.3readlines():按行输出所有内容
# f=open("test.txt")
# li=f.readlines()
# print(li)
# # print(f.readlines())#按行输出所有内容，输出的是列表格式['bingbing18\n', 'jasd\n', '\n', 'jasdfjaws\n', 'jasdlfgjlkasdf']
# # f.close()
# for i in li:
#     print(i)
#2.4.访问模式
#r（只读模式），r+（可读可写模式），w（只写模式），w+(可读可写模式),a(只写），a+(可读可写模式),后面四种模式都是若文件不存在可创建模式
# file=open("test.txt","w+")#这个默认是只读模式
# file.write("8907979808")#因为open打开后默认是只读模式，不能写
# #此时新增的内容输出不出来，因为新增内容后指针指向的是输入内容后一个位置，输出信息的时候是从指针位置往后进行输出的，想要解决很简单，把指针挪到开头就好了
# file.seek(0)#把指针挪到开头
# print(file.read())
# file.close()
#重点，r+情况下每次写都是对原信息的覆盖，不想覆盖想添加需要是a+模式下，但a+模式下是将写的内容添加到末尾
#w+是可读可写，w是写文件，但一打开就清空文件内容
#2.5文件定位操作
#tell()和seek()
#tell()显示文件指针当前位置
# file=open("test.txt","r+")
# file.write("hello")
# print(file.tell())
# file.close()
#没有元素的时候指针指向0，有n个元素的时候指针指向n对
#，seek(offset, whence) 两个参数：
  # - offset — 偏移量，正数往后、负数往前
  # - whence — 从哪开始算，默认 0,0作为开头作为参考位置，1代表当前位置作为参考位置，2代表末尾位置作为参考位置
 # │ 0      │ 从文件开头算 │ seek(5, 0) → 去第5个字节      │
 # ├────────┼──────────────┼─────────────────────────────────┤
 # │ 1      │ 从当前位置算 │ seek(3, 1) → 往后3个字节      │
 # ├────────┼──────────────┼─────────────────────────────────┤
 # │ 2      │ 从文件末尾算 │ seek(-10, 2) → 倒数第10个字节


#3.1 with open
#作用：代码执行完，系统会自动调用f.close(),可以省略关闭文件步骤
# with open("test.txt","w") as  f: #f是文件对象
#     f.write("hello world")
#print(f.read())#这个存在两个错误，第一个with语句一出标识着该文件已经被关闭，其次该文件的权限是写权限，该权限不能读
# print(f.closed)#True


#编码格式
#1.文件类的实例化对象中有个encoding参数，该参数用于指明打开文件时用的是什么编码方式
# with open(r"D:\Desktop\test.txt","r+",encoding="utf-8") as f:#windows系统默认是GBK编码方式
#     f.write("hello")
#     print(f.read())
# with open("test.txt","a+") as f:
#      f.write("hello world")
# with open("test1.txt","a+") as f1:
#     f1.write("hello world")
#     f1.seek(0)#因为a+模式下文件打开指针在末尾所以需要将指针移到最前端才能输出所有内容
#     print(f1.read())
    #print(f1.closed)#closed是文件对象的属性，不是方法，所以调用的时候不需要加（）

# 文本文件： 存的都是字符，按编码（UTF-8/GBK）翻译后你直接能读。如 .txt .py .json。
# 二进制文件： 存的是原始字节数据，不是给人读的。如 .exe .jpg .mp4
#案例:图片复制“rb”
"""
1.读取文件
图片是一个二进制文件，想要写入必须先拿到
2.写入图片
"""
# f=open(r"D:\Desktop\image1f.jpg","rb") #二进制文件不需要"编码破译"，它直接用 "rb" 读原始字节：rb就是 read binary 的缩写 — 以二进制方式读取文件
# # print(f.read())
# #将读取到的内容写入得到当前文件中
# with open(r"D:\python.test\Python01\image1.jpg","wb") as file:
#     file.write(f.read())
# f.close()

#导入模块
import os#os是操作系统接口模块，让python能和操作系统打交道
# import os
#   os.mkdir("new_folder")           # 创建文件夹
#   os.remove("test.txt")            # 删除文件
#   os.rename("old.txt", "new.txt")  # 重命名
#   os.path.exists("test.txt")       # 判断文件存在
#   os.listdir(".")                  # 列出当前目录所有文件
#   os.getcwd()                      # 获取当前工作目录
#1.文件重命名 os.rename(旧名字，新名字）
# os.rename(r"D:\Desktop\image1f.jpg", r"D:\Desktop\image.jpg")
#删除文件:os.remove("文件名")
# os.remove(r"D:\Desktop\image.jpg")
#创建文件夹：os.mkdir("文件夹名称") mkdir:makedirectory
# os.mkdir("hzs")
#4. 删除文件夹:rmdir(“文件夹名称”) rmdir：removedirectory
# os.rmdir("hzs")
#5.获取当前目录os.getcwd():Current Working Directory
# print(os.getcwd())
#6.获取目录列表os.listdir("文件夹地址和名称")
#print(os.listdir(r"D:\Desktop\Chatbox"))
# os.mkdir("py18")
# os.rmdir("py18")
