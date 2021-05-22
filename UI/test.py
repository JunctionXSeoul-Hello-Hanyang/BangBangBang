from BoardUI import BoardUI
import time

if __name__ == "__main__":
    myName = "me"
    playerName = {"1", "2", "3", "4"}
    # 기본 보드 생성
    # 시작시 무조건 생성해주어야함
    # myName에는 내 이름을, playerName에는 나머지 플레이어의 이름을 넣어주어야 한다.
    b = BoardUI(myName=myName, playerName=playerName)

    # drawEnemyStatus는 적 상태를 업데이트 하는 UI
    # 맨 앞에 있는 playerName으로 접근가능하다.
    # "me"와 같이 잘못된 이름이면 업데이트가 안됨
    # 성공하면 0, 실패하면 -1 을 리턴
    b.drawEnemyStatus("me", 1, 2, role="deputy", gun="appaloosa", equipment="barrel")

    b.drawEnemyStatus("1", 1, 2, role="outlaw", gun="appaloosa", equipment="barrel")
    b.drawEnemyStatus("2", 1, 2, role="outlaw",  gun="appaloosa")
    
    # role, gun, equipment는 기본 상태가 존재함. 인자로 넣어주지 않을 경우 기본 상태로 지정됨(기본 상태는 X 그림 또는 카드 뒷면)
    b.drawEnemyStatus("3", 1, 2)
    b.drawEnemyStatus("4", 1, 2)

    # 업데이트를 해준다음에는 반드시 drawBoard를 실행해주어야 새롭게 그림
    b.drawBoard()

    time.sleep(5)

    b.drawEnemyStatus("4", 1, 2, role="deputy",  gun="mustang", equipment="jail")
    b.drawEnemyStatus("1", 1, 2)
    b.drawBoard()

    time.sleep(100)