import socket
import threading
import socketserver
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    dic = {}
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data).encode('utf8')
        self.request.sendall(response)
        if data.decode('utf8').upper() == 'HOME':
            self.dic['home']=self.client_address
            print(self.dic['home'])
        if data.decode('utf8').upper() == 'GETHOME':
            if 'home' in self.dic:
                self.request.sendall(self.dic['home'].encode('utf8'))
            else :
                self.request.sendall('没有收到home地址'.encode('utf8'))

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
