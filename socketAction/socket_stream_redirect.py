#coding:utf-8
__author__ = 'similarface'

#############
#用于连接非GUI程序的标准流到一个套子节的工具一个GUI程序可以使用这与非GUI程序进行交互
#############


import sys
from socket import *
port = 50028
host = 'localhost'


def initListenerSocket(port=port):
    '''
    初始化监听程序
    :param port:端口
    :return:返回连接
    '''
    #获取sock对象
    sock=socket(AF_INET,SOCK_STREAM)
    #绑定主机和端口 非写成''  JB无语了
    sock.bind(('',port))
    #监听5个
    sock.listen(5)
    #获取连接
    conn,addr=sock.accept()
    return conn

def redirectOut(port=port,host=host):
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect((host, port))
    file=sock.makefile('w')
    sys.stdout=file
    return sock

# def redirectOut(port=port,host=host):
#     '''
#     在接收之前其他连接失败
#     连接调用者标准输出流到一个套子节
#     这个套子节用于GUI监听
#     在收听者启动后，启动调用者
#     :param port:
#     :param host:
#     :return:
#     '''
#     sock=socket(AF_INET,SOCK_STREAM)
#     sock.connect((host, port))
#     file=sock.makefile('w')
#     sys.stdout=file
#     return sock


def redirectIn(port=port,host=host):
    '''
    连接调用者标准输入流到
    :param port:
    :param host:
    :return:
    '''
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect((host, port))
    file=sock.makefile('r')
    sys.stdin=file
    return sock

def redirectBothAsClient(port=port,host=host):
    '''
    :param port:
    :param host:
    :return:
    '''
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect((host, port))
    ofile=sock.makefile('w')
    ifile=sock.makefile('r')
    sys.stdout=ofile
    sys.stdin=ifile
    return sock



def redirectBothAsServer(port=port,host=host):
    '''

    :param port:
    :param host:
    :return:
    '''
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind((host,port))
    conn,addr=sock.accept()
    ofile=conn.makefile('w')
    ifile=conn.makefile('r')
    sys.stdout=ofile
    sys.stdin=ifile
    return conn

