import random

class Dice():

    dice_st = 0
    dice_nd = 0
    dice_sum = 0
    dice_r = 0

    @classmethod
    def first_dice(cls):
        # 첫 번째 주사위 던지기 질문
        f_d = input("첫 번째 주사위던지기 (Y)")
        while f_d != 'Y':
            f_d = input("첫 번째 주사위던지기 (Y)")
        
        cls.dice_st = random.randint(1,6)
        print(f"첫번째 주사위의 개수는 {cls.dice_st}입니다.")
        next_throw = input("두번째 주사위를 던지시겠습니까?(Y/N)")
        #답변이 Y/N 이외의 경우 예외처리   
        while not(next_throw == "Y" or next_throw == "N"):
            next_throw = input("(Y/N) 중 하나를 입력해주십시오.(Y:던진다/N:던지지 않는다)")
        return cls.decision_di2(next_throw)  

    #두번째 주사위를 굴릴지 여부 결정
    @classmethod
    def decision_di2(cls, next_throw):
        if next_throw == "N":
            print(f"{cls.dice_st}칸 전진합니다.")
            cls.dice_r = cls.dice_st
            return cls.dice_r
        elif next_throw == "Y":
            # 두번째 주사위 함수 호출
            return cls.second_dice()

    # 두번째 주사위 굴리기/결과 값 판단
    @classmethod   
    def second_dice(cls):
        cls.dice_nd = random.randint(1,6)
        print(f"두번째 주사위의 개수는 {cls.dice_nd}입니다.")
        cls.dice_sum = cls.dice_st + cls.dice_nd
        if cls.dice_sum >= 8:
            print(f"두 주사위의 합이 {cls.dice_sum}(으)로 8 이상이므로 낙오됩니다.")
            cls.dice_r = 0
            return cls.dice_r
            # 말을 판에서 없애고 실제 위치값을 옮기는 함수호출
        else:
            cls.dice_r = cls.dice_st * cls.dice_nd
            print(f"두 주사위의 합이 {cls.dice_sum}(으)로 8 미만이므로 {cls.dice_r}칸 전진합니다.")
            return cls.dice_r
