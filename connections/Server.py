import socket
import pickle
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

def broadcast_board():
    for conn in playersSocket:
        conn.sendall(pickle.dumps(board))

def threaded_client(conn):
    # conn.send(str.encode("Connected"))
    
    reply = ""
    while True:
        # 여기선 서버의 경우 정보를 받는 경우에만 동작하게 된다. (턴제로)
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            
            print("Received: ", reply)
            print("Sending : ", reply)

            # 특정 함수 처리

            broadcast_board() # 변경 이후의 맵이 모든 클라이언트에 전달
        except:
            break

    print("Lost connection")
    conn.close()


def handle(reply):
    reply.name = reply.split(' ')

    if reply.name[0].equals("bang"):
    elif reply.name[0].equals("missed"):
    elif reply.name[0].equals("beer"):
    elif reply.name[0].equals("duel"):
    elif reply.name[0].equals("indian"):
    elif reply.name[0].equals("gatling"):
    elif reply.name[0].equals("saloon"):
    elif reply.name[0].equals("panic"):
    elif reply.name[0].equals("generalstore"):
    elif reply.name[0].equals("stagecoach"):
    elif reply.name[0].equals("wellsfargo"):
    elif reply.name[0].equals("catbalu"):


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    print(currentPlayer, "players connected")
    currentPlayer += 1
    playersSocket.append(conn);

    if currentPlayer == 5:
        print("Game Starting....")
        board = Board(5) # 게임판 생성
        broadcast_board() # 게임판 시작 점 전부 뿌림
        for conn in playersSocket:
            start_new_thread(threaded_client, (conn, ))




