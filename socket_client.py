# client  
  
from socket import *

class TcpClient:
    HOST='54.169.85.240'
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

    def client(self,message):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((self.HOST, self.PORT))
        try:
            sock.sendall(message.encode('utf8'))
            response = sock.recv(1024)
            print("Received: {}".format(response).encode('utf8')) 
        finally:
            sock.close()
            
if __name__ == '__main__':
    client=TcpClient()
    client.client("home")
