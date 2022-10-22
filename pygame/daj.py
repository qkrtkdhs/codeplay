eng =['a', 'b', 'c', 'b', 'd']
kor =['가', '나', '다', '라', '마']
ok = 0
running = True

while running:
    ok = 0
    for i in range(5):
        if kor[i] == input(f"{eng[i]}뜻 : "):
            print("O")
            ok += 1
            if ok == 5:
                running = False
        else:
            print("X")
            break
        print("끝")