# client  
  
from socket import *

class TcpClient:
    HOST='54.169.85.240'
    local = '127.0.0.1'
    PORT=22345
    BUFSIZ=1024
    ADDR=(HOST, PORT)
    def __init__(self):
        '''
        print("开始")
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        print(self.ADDR)
        while True:
            data=input('>')
            if not data:
                self.client.close()
                break
            self.client.send(data.encode('utf8'))
            data=self.client.recv(self.BUFSIZ)
            if not data:
                self.client.close()
                break
            print(data.decode('utf8'))'''
        pass

    def client(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.HOST, self.PORT))
        while True:
            try:
                message = input("来吧，输入\n")
                
                sock.sendall(message.encode('utf8'))
                response = sock.recv(1024)
                print(response.decode('utf8'))
                if message.upper() == "QUIT":
                    break
            except Exception as e:
                print(e)
                break;
        sock.close()
            
if __name__ == '__main__':
    client=TcpClient()
    client.client()
    
