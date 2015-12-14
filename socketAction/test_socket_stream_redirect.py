__author__ = 'similarface'
import sys, os, multiprocessing
from socket_stream_redirect import *
# def server1():
#     mypid = os.getpid()
#     conn = initListenerSocket()
#     file = conn.makefile('r')
#     for i in range(3):
#         data = file.readline().rstrip()
#         print('server %s got [%s]' % (mypid, data))


def server1():
    mypid=os.getpid()
    conn=initListenerSocket()
    file=conn.makefile('r')
    for i in range(3):
        data=file.readline().rstrip()
        print('Server %s got [%s] '%(mypid,data))

def client1():
    mypid=os.getpid()
    redirectOut()
    for i in range(3):
        print('client %s: %s' % (mypid, i))
        sys.stdout.flush()


if __name__ == '__main__':
    server=eval('server'+sys.argv[1])

    client=eval('client'+sys.argv[1])

    multiprocessing.Process(target=server).start()

    client()
    #import time; time.sleep(5)