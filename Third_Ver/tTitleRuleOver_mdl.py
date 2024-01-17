# <MAHe> # 게임을 시작합니다.(Y)
def title_print():
    print("""
    ___  ___  ___   _   _    __ 
    |  \/  | / _ \ | | | |  |_/   
    | .  . |/ /_\ \| |_| |  ___ 
    | |\/| ||  _  ||  _  | / _ \\
    | |  | || | | || | | ||  __/
    \_|  |_/\_| |_/\_| |_/ \___| 
    """)
def start_or_rule():
    start_q = input("   [ 게임 시작: Y / 규칙 안내: R ] ")
    while start_q != 'Y' and start_q != 'R':
        start_q = input("   [ 게임 시작: Y / 규칙 안내: R ] ")
        
    if start_q == 'R':
        # 규칙을 설명합니다.(R)
        print("""

        < 규칙 안내 >

        1. 한 턴마다 주사위를 1개씩 2개까지 굴릴 수 있습니다.

        2. 하나의 주사위만을 굴린다면 나온 주사위 눈 만큼 전진하며, 
           두 개의 주사위를 굴린다면 두 주사위 눈 수의 곱 만큼 전진합니다.

        3. 단, 두 개의 주사위를 굴렸을 때 눈 수의 합이 8이상일 경우 낙오되어 원점으로 돌아갑니다.

        4. 두 참가자가 같은 칸에 도착했을때 나중에 도착한 참가자가 기존의 참가자에게 업힐 수 있습니다. 
           업혔을 때는 다음 한 턴 동안 업은 참가자의 움직임을 따라갑니다.

        5. 1번 칸에 도달할 때마다 점수카드를 획득하며, 점수 카드에서는 2~5 중 랜덤으로 점수를 얻을 수 있습니다. 

        6. 총 10개의 점수카드가 존재하며, 마지막 점수 카드의 점수는 8로 고정됩니다.

        7. 10개의 점수카드가 모두 소진 되었을때 누적 점수가 높은 참가자가 승리합니다.
        
        """)
        while start_q != 'Y':
            start_q = input(" [ 게임 시작: Y ] ")
        

# 점수 계산 및 승리자 출력 함수 

def Game_over(p1_info, p2_info):
    print(" < 게임 결과 > ")
    print(" 참가자 %s의 총점 %d점 "%(p1_info['nickname'],p1_info['score']))
    print(" 참가자 %s의 총점 %d점 "%(p2_info['nickname'],p2_info['score']))
    print("---------------------------------------------------------")

    if p1_info['score'] > p2_info['score']:
        print(" 축하드립니다! %s의 승리입니다. " %(p1_info['nickname']))
    elif p1_info['score'] < p2_info['score']:
        print(" 축하드립니다! %s의 승리입니다. " %(p2_info['nickname']))
    else:
        print(" 무승부입니다. ")
    print("---------------------------------------------------------")
