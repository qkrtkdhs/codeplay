# s1 = 0
# s2 = 0
# s3 = 0
# d = input("제시어 입력 : ")

# s1 = (d[0])
# s1d = input(s1 + " : ")
# if (s1d[0]) == s1:
#     pass
# else:
#     print("수준봐라ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

# s2 = (d[1])
# s2d = input(s2 + " : ")
# if (s2d[0]) == s2:
#     pass
# else:
#     print("수준봐라ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

# s3 = (d[2])
# s3d = input(s3 + " : ")
# if (s3d[0]) == s3:
#     pass
# else:
#     print("수준봐라ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

def shs(words):
    words = ""
    poem = []
    wi = ""
    words = input("제시어 입력 : ")

    for word in words:
        print(f"{word} - ")
        while True:
            wi = input("입력 : ")
            if word == wi[0]:
                poem.append(wi)
                break
            else:
                print("틀림ㅋㅋㅋㅋㅋ")
    for i in range(3):
        print(f"{words[i]} : {poem[i]}")

shs(input("입력 : "))