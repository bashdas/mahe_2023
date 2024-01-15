import tTitleRuleOver_mdl as TRO
from tSquare_cls import *
from tPlayer_cls import *
from tCard_cls import *
from tDice_cls import *

# <MAHe> # 게임을 시작합니다.
TRO.title_print()
TRO.start_or_rule()

# 각각의 플레이어를 생성 후 플레이어 닉네임을 입력받아 저장합니다.
p1 = Player()
print(" <첫 번째 참가자 정보 입력> ")
p1.nk_name_in()

p2 = Player()
print(" <두 번째 참가자 정보 입력> ")
p2.nk_name_in()

# 닉네임이 중복되지 않게 예외처리
while p1.info['nickname'] == p2.info['nickname']:
    print(" 중복된 닉네임입니다. 다시 입력해주세요. ")
    print(" <두 번째 참가자 정보 입력> ")
    p2.nk_name_in()

# 초기 ground 출력
square = Square()
ground = square.create_ground()

square.print_ground(ground)

while Card.__remain_card != 0:
##########################################################

    # p1가 먼저 주사위를 던집니다. di_result 값을 p1 정보에 저장합니다.
    print(f" {p1.info['nickname']}의 차례입니다. ")
    p1.info['di_result'] = Dice.first_dice()
    
    # p1.di_result 값을 가지고 말 이동 계산
    square.move_update(p1.info, p2.info)

    # p1이 점수카드를 얻을 수 있는지 판단, 지급
    Card.judge_g_card(p1.info, p2.info)

    # p1.loc 값을 가지고 Square 클래스 호출 후 말 이동 반영 출력
    square.player_on_ground(ground, p1.info, p2.info)

    ##########################################################

    if Card.__remain_card == 0:
        break

    # p2의 차례, 주사위를 던진 후 di_result 값을 p2 정보에 저장합니다.
    print(f" {p2.info['nickname']}의 차례입니다. ")
    p2.info['di_result'] = Dice.first_dice()
    
    # p2.di_result 값을 가지고 말 이동 계산
    square.move_update(p2.info, p1.info)

    # p2가 점수카드를 얻을 수 있는지 판단, 지급
    Card.judge_g_card(p2.info, p1.info)

    # p2.loc 값을 가지고 Square 클래스 호출 후 말 이동 반영 출력
    square.player_on_ground(ground, p2.info, p1.info)

##########################################################
# 게임 종료
TRO.Game_over(p1.info, p2.info)