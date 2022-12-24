import random
numbers = []
su = 0

while len(numbers) < 10:
    su = random.randint(1, 100)
    if su in numbers:
        continue
    else:
        numbers.append(su)
while True:
    jrid = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            jrid += 1
    if jrid == 0:
        break
print(numbers)