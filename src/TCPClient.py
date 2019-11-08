import socket

class TCPClient(object):
    def __init__(self, autoSplit, ip, port):
        self.AutoSplit = autoSplit
        self.socket = None
        self.remote_ip = ip
        self.remote_port = port
        self.buffer_size = 1024
        self.data = None
        self.isStart = False
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.remote_ip, self.remote_port))
        self.socket.setblocking(0)
        self.isStart = True
    def close(self):
        self.socket.close()
    def read(self):
        if self.isStart:
            try:
                # The buffer will be clean once it have been succefully readed
                self.data = self.socket.recv(self.buffer_size)
                return self.data
            except:
                return b''
                pass
            pass
    pass