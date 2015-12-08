#coding:utf-8
__author__ = 'similarface'
from socket import *
#连接的目标主机
HOST='127.0.0.1'
#联机的的目标端口
PORT=50070
#消息
message=[u'Having You meat?']
#socket对象
socketObj=socket(AF_INET,SOCK_STREAM)
#socket连接
socketObj.connect((HOST,PORT))
#
while True:
    message=raw_input()
    #发消息
    socketObj.send(message)
    #接收消息
    data=socketObj.recv(1024)
    print('对方: '+data)