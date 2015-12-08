#coding:utf-8
__author__ = 'similarface'
'''
客服端的事务相对短暂
'''

import sys,time
from select import select
from socket import socket,AF_INET,SOCK_STREAM

def now():return time.ctime(time.time())

HOST=""
PORT=50007

numPortSocks=2

mainsocks,readsocks,writesocks=[],[],[]

for i  in range(numPortSocks):
    portsock=socket(AF_INET,SOCK_STREAM)
    portsock.bind((HOST,PORT))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    PORT+=1

print('Select-server loop starting')

while True:
    readables,writeables,exceptions=select(readsocks,writesocks,[])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock,address=sockobj.accept()
            print('Connect:',address,id(newsock))
            readsocks.append(newsock)
        else:
            data=sockobj.recv(1024)
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply='Echo=>%s at %s' % (data,now())
                sockobj.send(reply.encode())