import random

class Card():
    # '__'을 이용한 클래스 외부 접근 차단
    __remain_card = 10

    @classmethod
    def judge_g_card(cls, info_d, info_o):
        if info_d['block_count'] > 20:
                info_d['block_count'] -= 20
                print(f" {info_d['nickname']}가 원점을 지나 점수 카드를 한 장 획득합니다. ")
                cls.get_card(info_d)
                if info_o['block_count'] > 20 and cls.__remain_card > 0:
                    info_o['block_count'] -= 20
                    print(f" {info_d['nickname']}에게 업힌 상태로 원점을 지나 ")
                    print(f" {info_o['nickname']}도 점수 카드를 한 장 획득합니다. ")
                    cls.get_card(info_o)
        else:
            print(f" 남은 점수 카드의 개수는 {cls.__remain_card}개 입니다. ")            

    @classmethod
    def get_card(cls, info): 
        # 점수 카드 한 장 획득, 마지막 8점 카드 획득 시 게임 종료
        if 1< cls.__remain_card <=10:
            new_get = random.randint(2,5)
            info['score'] += new_get
            cls.__remain_card -= 1
            print(" 점수 카드의 점수: %d 점 "%(new_get))
            print(f" 남은 점수 카드의 개수는 {cls.__remain_card}개 입니다. ")   
        elif cls.__remain_card == 1:
            cls.__remain_card -= 1
            info['score'] += 8
            print(" 점수 카드의 점수: 8점 ")
            print(f" 남은 점수 카드의 개수는 {cls.__remain_card}개 입니다. ")   
            print(" 게임이 종료되었습니다. ")
            # 게임 종료 
