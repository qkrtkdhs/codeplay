f = open("test.txt", "a", encoding = "UTF-8")

f.write("정상" + "\n")
f.write("수" + "\n")

# words = []
# for i in f.readlines():
#     words.append(i.strrip("파"))
# print(words)
f.close()