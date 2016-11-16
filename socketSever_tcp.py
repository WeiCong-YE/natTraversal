import SocketServer
class MyTCPHandler(SocketServer.BaseRequestHandler): #定义request handler类，从BaseRequestHandler类继承

    def handle(self): #复写handle()方法，注意：该方法必须复写，用于处理当前的request
        self.data = self.request.recv(1024).strip() #self.request是和客户端连接的套接字，可直接使用
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())

class MyTCPHandler(SocketServer.StreamRequestHandler): #定义request handler类，从StreamRequestHandler类继承

    def handle(self):
        self.data = self.rfile.readline().strip() #self.rfile/self.wfile是文件格式类型的socket，相当于对原始socket的封装，让读写网络数据向读写文件一样容易
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.wfile.write(self.data.upper())     

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler) #传入监听地址、端口号和request handler类
    server.serve_forever() #启动监听处理request
