import socket
import pickle

class Network:
    def __init__(self, serverIp, serverPort):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = serverIp
        self.port = serverPort
        self.addr = (self.server, self.port)
        self.board = None
        self.id = self.connect()

        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.board = pickle.loads(self.client.recv(4096))
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.client.close()
        except Exception as e:
            print(e)


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)