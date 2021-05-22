import socket


class Network:
    def __init__(self, serverIp, serverPort):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.client)
        self.server = serverIp
        self.port = serverPort
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)
            pass

    def close(self):
        try:
            self.client.close()
        except:
            pass


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)