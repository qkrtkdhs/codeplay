drinks = {"비타500" : 700, "비락식혜" : 1500, "레몬워터" : 1700, "포카리스웨트" : 1800, "에비앙" : 15000}
money = 0
pick = 0

def showcase():
    print("[음료선택]")
    print(drinks)
    print("[", "-" * 13, "]")

order = True

while True:
    showcase()
    input("[주문]")
    while  True:
        if money > 0:
            pass
        else:
            money = input("[돈 투입] - [종료:X]")
        if money == "X":
            break
        showcase()
        pick = input("[음료선택] - ")
        if pick == "X":
            break
        elif int(money) >= drinks[pick]:
            print(f"[주문하신 {pick} 나왔습니다]")
            money = int(money) - drinks[pick]
        else:
            print("[잔액 부족]")
            continue
    if int(money) > 0:
        print(f"[거스름돈{money}원]")
        print("[안녕히가세요]")
        money = 0