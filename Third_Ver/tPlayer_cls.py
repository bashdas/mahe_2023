class Player:

    def __init__(self):
        self.info = {'nickname':'x', 'score':0, 'ride':0, 'loc':0, 'block_count':0, 'di_result':0}

    def nk_name_in(self):
        N = input(" 닉네임을 입력하세요(한 개의 문자로 표현): ")
        while len(N) != 1 or not isinstance(N, str):
            print(" 숫자가 아닌 하나의 문자열로 적어주세요. (예시: A, B, 해, 달, 별, 꽃) ")   
            N = input(" 닉네임을 입력하세요(한 개의 문자로 표현): ")
        self.info['nickname'] = N   
    # 닉네임 중복 예외처리는  g_manager에서 처리   