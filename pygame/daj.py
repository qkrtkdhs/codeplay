import random
def wordMemorize():
    eng =['a', 'b', 'c', 'b', 'd']
    kor =['가', '나', '다', '라', '마']
    pick = 0
    score = 0
    answer = 0

    while len(eng) > 0:
        pick = random.randint(0, len(kor) - 1)
        score += 1
        answer = input(f"{kor[pick]} ←  이거 영어로 : ")
        if answer == eng[pick]:
            print("ㅇ")
            kor.pop(pick)
            eng.pop(pick)
        else:
            print("ㄴ")

    print("클리어") 
    if score < 6:
        print("클리어라고")
    elif 5 < score < 9:
        print("혹시 초등학생?")
    else:
        print("사람임?")

    


