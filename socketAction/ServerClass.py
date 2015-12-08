#coding:utf-8
__author__ = 'similarface'

import SocketServer,time
HOST=""
PORT=50070
def now():
    return time.ctime(time.time())

class MyClientHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print(self.client_address,now())
        while True:
            data=self.request.recv(1024)
            if not data:break
            reply='Echo=>%s at %s' %(data,now())
            self.request.send(reply.encode())
        self.request.close

myaddr=(HOST,PORT)
server=SocketServer.ThreadingTCPServer(myaddr,MyClientHandler)
server.serve_forever()