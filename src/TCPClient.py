import socket
from icommunication import icommunication

class TCPClient(icommunication):
    def __init__(self, autoSplit):
        self.AutoSplit = autoSplit
        self.socket = None
        self.remote_ip = '127.0.0.1'
        self.remote_port = 16834
        self.buffer_size = 1024
        self.data = None
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.remote_ip, self.remote_port))
        self.socket.setblocking(0)
    def close(self):
        self.socket.close()
    def read(self):
        try:
            # The buffer will be clean once it have been succefully readed
            self.data = self.socket.recv(self.buffer_size)
            return self.data
        except:
            return b''
            pass
        pass
    pass