def word_in ():
    hd = open("kr.txt", "a", encoding = "UTF-8")
    yd = open("eg.txt", "a", encoding = "UTF-8")

    while True:
        word = input("한글 입력(종료-q):")
        if word == "q":
            break
        else:
            hd.write(word+ "\n")

        word = input("영어 입력(종료-q):")
        if word == "q":
            break
        else:
            yd.write(word+ "\n")
def exam():

    hd = open("kr.txt", "r", encoding = "UTF-8")
    yd = open("eg.txt", "r", encoding = "UTF-8")
    score = 0
    kw = []
    ew = []

    for r in hd.readlines():
        kw.append(r.strip())
    for r in yd.readlines():
        ew.append(r.strip())

    for i in len(kw):
        answer = input(f"{kw[i]} 뜻 : ")
        if answer == ew[i]:
            print("정답")
            score += 1
        else:
            print(f"오답. 답 = {ew[i]}")
    print(f"끝! - {len(kw)}중 정답{score}개")
    if score == len(kw):
        print("만점ㅊㅎ")
    else:
        print("수준ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

    hd.close()
    yd.close()

while True:
    mode = int(input("1 = 단어입력, 2.시험, 3.종료"))
    if mode == 1:
        word_in()
    elif mode == 2:
        exam()
    elif mode == 3:
        break
    else:
        print("뭐라는겨")