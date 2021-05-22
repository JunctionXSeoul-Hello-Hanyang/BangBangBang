from BoardUI import BoardUI
import time

if __name__ == "__main__":
    myName = "me"
    playerName = {"1", "2", "3", "4"}
    # 기본 보드 생성
    b = BoardUI(myName=myName, playerName=playerName)
    # 특정 위치에 카드 그리기
    # b.drawCard("Sheriff", "player1")
    b.drawEnemyStatus("me", 1, 2, role="deputy")
    b.drawEnemyStatus("1", 1, 2, role="outlaw")
    b.drawEnemyStatus("2", 1, 2, role="outlaw")
    b.drawEnemyStatus("3", 1, 2)
    b.drawEnemyStatus("4", 1, 2)

    b.drawBoard()
    time.sleep(100)
