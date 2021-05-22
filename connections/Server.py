import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import socket
import pickle
import random
from _thread import *
from Rule import Board


server = "0.0.0.0"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(5)
print("Waiting for a connection, Server Started")

playersSocket = []
currentPlayer = 0
board = None


# 차례를 넘길 시 시행하는 함수
def turnover():
    nextTurn = board.whoseTurn + 1;
    for _ in range(4):
        if nextTurn == 5:
            nextTurn = 0

        player = board.players[nextTurn]
        if player.field.bullets > 0:
            board.whoseTurn = nextTurn
            break
        nextTurn += 1
    drawCard()
    drawCard()

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
        print(conn)
        conn.sendall(pickle.dumps(board))

def threaded_client(conn, currentPlayer):
    conn.send(str.encode(str(currentPlayer)))

    reply = ""
    while True:
        # 여기선 서버의 경우 정보를 받는 경우에만 동작하게 된다. (턴제로)
        try:
            data = conn.recv(4096)

            if not data:
                print("Disconnected")
                break
            reply = data.decode("utf-8")

            if reply == 'update':
                None
            elif reply == 'turn over':
                turnover()
            else:
                handle(reply)

            print(reply)

            conn.send(pickle.dumps(board))

            # broadcast_board() # 변경 이후의 맵이 모든 클라이언트에 전달
        except:
            break

    print("Lost connection")
    conn.close()


def handle(reply):
    splitedCmd = reply.split(' ')
    
    usedCardIdx = int(splitedCmd[1])

    if splitedCmd[0] == 'bang':
        enemyPlayerIdx = int(splitedCmd[2])
        actionBang(enemyPlayerIdx)

    elif splitedCmd[0] == 'beer':
        actionBeer()

    elif splitedCmd[0] == 'duel':
        enemyPlayerIdx = int(splitedCmd[2])
        actionDuel(enemyPlayerIdx)

    elif splitedCmd[0] == 'indian':
        actionIndian()

    elif splitedCmd[0] == 'gatling':
        actionGatling()

    elif splitedCmd[0] == 'saloon':
        actionSaloon()

    elif splitedCmd[0] == 'panic':
        cardIndex = int(splitedCmd[2])
        actionPanic(cardIndex)

    elif splitedCmd[0] == 'catBalu':
        cardIndex = int(splitedCmd[2])
        actionCalbalou(cardIndex)

    elif splitedCmd[0] == 'generalStore':
        actionEmporio()

    elif splitedCmd[0] == 'stagecoach':
        actionDiligenza()
        
    elif splitedCmd[0] == 'wellsFargo':
        actionWellsPargo()

    handleAfterCardUsase(usedCardIdx)



# 자신의 생명력을 1 올림 (최대 최력 이상 불가)
def actionBeer():
    player = board.players[board.whoseTurn]
    # 보안관은 5, 나머지는 4가 최대
    field = player.field
    if field.bullets > 0:
        if field.role == 'Sheriff':
            if field.bullets < 5:
                field.bullets += 1
        else:
            if field.bullets < 4:
                field.bullets += 1

# 사용한 사람 제외 뱅을 한 장씩 버려야하며, 못버리면 생명력 1 하락
def actionIndian():
    for idx, player in enumerate(board.players):
        if idx == board.whoseTurn:
            continue # 자기 자신은 제외

        hasMissed = False

        # 빗나감이 있는 경우 무조건 내며 다음 차례로간다.
        for cardIdx, card in enumerate(player.cards):
            if card.name == 'bang':
                board.trashCan.append(card)
                del player.cards[cardIdx]
                hasMissed = True
                break

        # 못 낸 경우 생명력 -1
        if not hasMissed:
            player.field.bullets -= 1

# 카드 두 장 가져오는 함수
def actionDiligenza():
    drawCard()
    drawCard()

# 카드 세 장 가져오는 함수
def actionWellsPargo():
    drawCard()
    drawCard()
    drawCard()

# 죽지 않은 모든 플레이어 생명력 1 상승
def actionSaloon():
    for player in board.players:
        # 보안관은 5, 나머지는 4가 최대
        field = player.field
        if field.bullets > 0:
            if field.role == 'Sheriff':
                if field.bullets < 5:
                    field.bullets += 1
            else:
                if field.bullets < 4:
                    field.bullets += 1

# 특정 패를 내 패로 만듦
def actionPanic(cardIndex):
    curPlayer = board.players[board.whoseTurn]

    isFind = False

    for player in board.players:
        for idx, card in enumerate(player.cards):
            if card.idx == cardIndex:
                curPlayer.cards.append(card) # 현재 플레이어에게 카드 넣어줌
                del player.cards[idx] # 원래 갖고 있던 플레이어에게 카드 삭제
                isFind = True

            if isFind:
                break
        if isFind:
            break

# 사용한 사람 제외 빗나감 내야하며, 못할 시엔 생명력을 1 잃는다.
def actionGatling():
    for idx, player in enumerate(board.players):
        if idx == board.whoseTurn:
            continue # 자기 자신은 제외

        hasMissed = False

        # 빗나감이 있는 경우 무조건 내며 다음 차례로간다.
        for cardIdx, card in enumerate(player.cards):
            if card.name == 'missed':
                board.trashCan.append(card)
                del player.cards[cardIdx]
                hasMissed = True
                break

        # 못 낸 경우 생명력 -1
        if not hasMissed:
            player.field.bullets -= 1

# 모든 참여자가 랜덤하게 한 장씩 갖게 된다.
def actionEmporio():
    for player in board.players:
        if player.field.bullets <= 0:
            continue # 죽은사람 제외
        
        # deck에서 카드 한 개 뽑음
        drawedCard = board.deck.pop()

        targetPlayer = board.players[board.whoseTurn]
        targetPlayer.cards.append(drawedCard)

        # deck 비어있는 경우, 버려진 덱을 섞어서 채워준다.
        if not board.deck:
            random.shuffle(board.trashCan)
            board.deck = board.trashCan
            board.trashCan = []

# 지정한 플레리어와 '뱅'의 개수를 두고 내기
def actionDuel(enemyPlayerIdx):
    curPlayer = board.players[board.whoseTurn]
    enemyPlayer = board.players[enemyPlayerIdx]
    
    curBangNum = 0 
    enemyBangNum = 0
    
    # 뱅 카드 전부 버리며 개수비교
    for idx, card in enumerate(curPlayer.cards):
        if card.name == 'bang':
            curBangNum += 1
            board.trashCan.append(card)
            del curPlayer.cards[idx]
    
    for idx, card in enumerate(enemyPlayer.cards):
        if card.name == 'bang':
            enemyBangNum += 1
            board.trashCan.append(card)
            del enemyPlayer.cards[idx]
            
    
    diff = curBangNum - enemyBangNum
    
    if diff > 0:
        enemyPlayer.field.bullets -= diff
    elif diff < 0:
        curPlayer.field.bullets += diff

# 뱅 사용 시 상대방이 빗나감 있는 경우 상쇄, 없는 경우 생명력 1 잃음
def actionBang(enemyPlayerIdx):
    enemyPlayer = board.players[enemyPlayerIdx]

    hasMissed = False

    for idx, card in enumerate(enemyPlayer.cards):
        if card.name == 'missed':
            board.trashCan.append(card)
            del enemyPlayer.cards[idx]
            hasMissed = True
            break

    if not hasMissed:
        enemyPlayer.field.bullets -= 1

# 특정 패를 내 패로 만듦 Panico와 동일하게 행동함
def actionCalbalou(cardIndex):
    curPlayer = board.players[board.whoseTurn]

    isFind = False

    for player in board.players:
        for idx, card in enumerate(player.cards):
            if card.idx == cardIndex:
                curPlayer.cards.append(card) # 현재 플레이어에게 카드 넣어줌
                del player.cards[idx] # 원래 갖고 있던 플레이어에게 카드 삭제
                isFind = True

            if isFind:
                break
        if isFind:
            break



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    currentPlayer += 1
    print(currentPlayer, "players connected")
    playersSocket.append(conn)

    if currentPlayer == 5:
        print("Game Starting....")
        board = Board.Board(5) # 게임판 생성
        drawCard()
        drawCard()
        #broadcast_board() # 게임판 시작 점 전부 뿌림

        for idx, conn in enumerate(playersSocket):
            start_new_thread(threaded_client, (conn, idx))




