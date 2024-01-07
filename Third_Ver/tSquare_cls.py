class Square():

    def move_update(info_d, info_o): 
        # dice_r 값이 낙오(0)인 경우 loc값과 b_c값 변경
        if info_d['dice_r'] == 0:
            info_d['loc'] = 0
            info_d['block_count'] = 0
        # block_count 값이 20일때 loc 값이 0이 되는 예외 처리
        elif info_d['block_count'] + info_d['dice_r'] == 20:
                info_d['loc'] = 20
        else:       
            info_d['block_count'] += info_d['dice_r']
            info_d['loc'] = info_d['block_count'] % 20

        # 올라탄 경우 동시이동과 그 다음 턴의 분리이동 구현
        if info_d['ride'] > 0:
            info_o['block_count'] = info_d['block_count']
            info_o['loc'] = info_d['loc']
            info_o['ride'] = 0
            info_d['ride'] = 0

        elif info_o['loc'] == info_d['loc'] and info_o['ride'] == 0 and info_d['ride'] == 0 and info_d['loc'] != 0:
            print(f"{info_d['nickname']}가 {info_o['nickname']}에게 업혔습니다.")
            print(f"한 차례동안 {info_o['nickname']}의 움직임을 따라갑니다.")
            info_o['ride'] = 1
            info_d['ride'] = 2          

    @classmethod
    def create_ground(cls):
        rows = 6
        cols = 6
        ground = [[0] * cols for _ in range(rows)]

        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        current_number = 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ground[top][i] = current_number
                current_number += 1
            top += 1

            for i in range(top, bottom + 1):
                ground[i][right] = current_number
                current_number += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ground[bottom][i] = current_number
                    current_number += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ground[i][left] = current_number
                    current_number += 1
                left += 1

        return ground

    @classmethod
    def print_ground(cls, ground):
        for row in ground:
            for element in row:
                print(element if element in range(1,21) else "■■", end=" ")
                print(' ' if element in range(1,7) else "", end=" " )
            print()

    @classmethod
    def player_on_ground(cls, ground, info_p1, info_p2):
        for row in ground:
            for element in row:
                print(element if element in range(1,21) and element not in [info_p1['loc'], info_p2['loc']] else "", end="")
                print("" if element in range(1,21) else "■■", end=" ")
                print(' ' if element in range(1,7) and element not in [info_p1['loc'], info_p2['loc']] else "", end="")
                print(info_p1['nickname'] if element is info_p1['loc'] else "", end=" ")
                print(info_p2['nickname'] if element is info_p2['loc'] else "", end=" ")                
            print() 
        print("-----------------------------------------------------")       