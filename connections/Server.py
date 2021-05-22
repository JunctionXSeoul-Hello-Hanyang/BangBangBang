import socket
from _thread import *

import sys

server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

playersSocket = []
currentPlayer = 0
board = None

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    
    # 맨 처음 게임판을 전달하는 작업
    conn.sendall('전달해야되는 값')

    reply = ""
    while True:
        # 여기선 서버의 경우 정보를 받는 경우에만 동작하게 된다. (턴제로)
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

def broadcast_board(board):



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    print(currentPlayer, "players connected")
    currentPlayer += 1
    playersSocket.append(conn);

    if currentPlayer == 5:
        print("Game Starting....")
        board = Board(5) # 게임판 생성
        for conn in playersSocket:
            start_new_thread(threaded_client, (conn, ))




