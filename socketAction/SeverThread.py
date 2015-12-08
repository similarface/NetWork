#coding:utf-8
__author__ = 'similarface'
'''
派生线程来处理
'''
import time
import os,sys,thread
from socket import *
#主机
HOST=""
#监听端口
PORT=50070
#新建立socket对象
socketObj=socket(AF_INET,SOCK_STREAM)
#对象要有作用对象
socketObj.bind((HOST,PORT))
#监听5个
socketObj.listen(5)

#当前时间 ep:'Mon Dec  7 11:23:59 2015'
def now():
    return time.ctime(time.time())

def handleClient(connection):
    while True:
        data=connection.recv(1024)
        if not data:break
        reply='Echo=>%s at %s' % (data,now())
        connection.send(reply.encode())
    connection.close()
    #子进程推出使用_exit os.exit回事全部结束
    os._exit(0)

def dispathcer():
    while True:
        connection,address=socketObj.accept()
        print(address)
        #使用线程来处理操作
        thread.start_new_thread(handleClient,(connection,))

dispathcer()