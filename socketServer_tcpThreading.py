import socket
import threading
import socketserver
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    dic = {}
    def handle(self):
        while True:
            data = self.request.recv(1024)
            cur_thread = threading.current_thread()
            response = "{}: {}".format(cur_thread.name, data)
            if data.decode('utf8').upper() == 'HOME':
                self.dic['home']=self.client_address
                response += '\n' + repr(self.dic['home'])
                print(self.dic['home'])
            if data.decode('utf8').upper() == 'GETHOME':
                print('收到得到homeip的请求')
                if 'home' in self.dic:
                    print("i have a home")
                    response += '\n' + repr(self.dic['home'])
                    print(repr(self.dic['home']))
                else :
                    print("找不到home的ip啊")
                    response += '没有收到home的连接'
            self.request.sendall(response.encode('utf8')) 
            if data.decode('utf8').upper() == 'QUIT' or data.decode('utf8').upper() == 'EXIT' :
                print("退出")
                break
        self.request.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):#继承ThreadingMixIn表示使用多线程处理request，注意这两个类的继承顺序不能变
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message.encode('utf8'))
        response = sock.recv(1024)
        print("Received: {}".format(response)) 
    finally:
        sock.close()

if __name__ == "__main__":
    HOST, PORT = "", 22345
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    #daemon_threads指示服务器是否要等待线程终止，要是线程互相独立，必须要设置为True，默认是False。
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    while True:
        pass
