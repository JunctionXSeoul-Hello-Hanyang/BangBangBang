import socket
import threading

asdf = 1

class testThread(threading.Thread):
    def __init__(self, client_socket, addr):
        super().__init__()
        self.client_socket = client_socket
        self.addr = addr 

    def run(self):
        print(asdf)

HOST = '127.0.0.1'

PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

lists = []
server_socket.listen()

for i in range(0, 2):
    #client_socket, addr = server_socket.accept()
    client_socket, addr = 1, 2

    t = testThread(client_socket, addr)
    t.start()
