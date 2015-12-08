#coding:utf-8
__author__ = 'similarface'
'''
使用进程进行分布式服务
'''
import time
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

#当前时间 ep:'Mon Dec  7 11:23:59 2015'
def now():
    return time.ctime(time.time())

#存活的子进程
activeChildren=[]


def reapChildren():
    #存在有存活的子进程
    while activeChildren:
        #os.waitpid等待一个指定的pid的子进程完成, 返回一个tuple返回它的进程id和退出状态 . 一般情况下option设为0.
        #第一个参数大于0，则waitpid会等待该pid结束，如果第一个参数是-1，则会等候所有子进程
        pid,stat=os.waitpid(0,os.WNOHANG)
        if not pid:break
        #移除
        activeChildren.remove(pid)

def handleClient(connection):
    time.sleep(5)
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
        reapChildren()
        childPid=os.fork()
        if childPid==0:
            #0为子进程
            handleClient(connection)
        else:
            #父进程中返回子进程的ID
            activeChildren.append(childPid)

dispathcer()