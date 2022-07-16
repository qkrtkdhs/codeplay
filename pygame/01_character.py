from operator import truediv
import random
character = []
running = True

while running:
    character_name = input("데이터 입력 : ")
    if character_name == "목록":
        for name in character:
            print(name)
    elif character_name == "추천":
        recommend = character[random.randint(0, len(character))]
        print("{}추".format(recommend))
    elif character_name == "끝":
        print("ㅂ2")
        running = False
    else:
        if len(character) == 10:
            print("10개넘음")
        else:
            character.append(character_name) 
    
