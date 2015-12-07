#coding:utf-8
__author__ = 'similarface'

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
#监听后处理
while True:
    #返回链接 和 地址
    connection,address=socketObj.accept()
    while True:
        data=connection.recv(1024)
        if not data:break
        print("对方: "+data)
        message=raw_input()
        #print('')
        connection.send(message)
    connection.close()