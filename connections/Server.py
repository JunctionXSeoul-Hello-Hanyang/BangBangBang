import socket
import pickle
import random
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

# 현재 순서의 플레이어가 카드 한 장 뽑는 함수
def drawCard():
    # deck에서 카드 한 개 뽑음
    drawedCard = board.deck.pop()

    # 현재 차례의 플레이어를 선택해 해당 플레이어의 덱에 추가해준다.
    curPlayer = board.players[board.whoseTurn]
    curPlayer.cards.append(drawedCard)

    # deck 비어있는 경우, 버려진 덱을 섞어서 채워준다.
    if not board.deck:
        random.shuffle(board.trashCan)
        board.deck = board.trashCan
        board.trashCan = []


# 카드 사용 후에 버리는 함수
# 매개변수의 경우 카드의 유니크 idx를 받는다.
def handleAfterCardUsase(cardIdx):
    curPlayer = board.players[board.whoseTurn]
    for idx, card in enumerate(curPlayer.cards):
        if card.idx == cardIdx:
            board.trashCan.append(card) # 버려질 쓰레기통에 카드 삽입
            del curPlayer.cards[idx] # 자신의 덱에서 카드 삭제




def broadcast_board():
    for conn in playersSocket:
        conn.sendall(pickle.dumps(board))

def threaded_client(conn, currentPlayer):
    conn.send(str.encode(str(currentPlayer)))
    
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

            handle(reply)

            # 특정 함수 처리

            broadcast_board() # 변경 이후의 맵이 모든 클라이언트에 전달
        except:
            break

    print("Lost connection")
    conn.close()


def handle(reply):
    splitedCmd = reply.split(' ')

    if splitedCmd[0].equals("bang"):
        actionBang(splitedCmd[1], splitedCmd[2], splitedCmd[3])
    elif splitedCmd[0].equals("missed"):
        actionMissed(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("beer"):
        actionBeer(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("duel"):
        actionDuel(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("indian"):
        actionIndian(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("gatling"):
        actionGatling(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("saloon"):
        actionSaloon(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("panic"):
        actionPanic(splitedCmd[1], splitedCmd[2], splitedCmd[3])
    elif splitedCmd[0].equals("generalstore"):
        actionGeneralStore(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("stagecoach"):
        actionStageCoach(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("wellsfargo"):
        actionWellsfargo(splitedCmd[1], splitedCmd[2])
    elif splitedCmd[0].equals("catbalu"):
        actionCatbalu(splitedCmd[1], splitedCmd[2], splitedCmd[3])

def actionBang(fromIndex, toIndex, cardIndex):
    board.handleAfterCardUsage(cardIndex)
    board.whoseTurn=toIndex
    board.phase="banged"

    board.players[toIndex].field.bullets = board.players[toIndex].field.bullets-1
    
def actionBeer(fromIndex, cardIndex)
    



def actionCatbalu(cardIdx):




while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    print(currentPlayer, "players connected")
    currentPlayer += 1
    playersSocket.append(conn, currentPlayer);

    if currentPlayer == 5:
        print("Game Starting....")
        board = Board(5) # 게임판 생성
        broadcast_board() # 게임판 시작 점 전부 뿌림
        for conn in playersSocket:
            start_new_thread(threaded_client, (conn, ))




