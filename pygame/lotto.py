import random
num =[]
dc = []
pick = 0
for i in range(1, 46):
    num.append(i)

print("이번주 로또 1등 번호는")

for j in range(7):
    pick = num.pop(random.randint(0, len(num) - 1))
    dc.append(pick)

print(dc)