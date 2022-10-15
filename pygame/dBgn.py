num_A = 0
num_B = 0
giho = 0
result = 0

num_A = input("1수")
num_B = input("2수")
giho = input("+-/*")

if giho == "+":
    resurt = num_A + num_B
elif giho == "-":
    resurt = num_A - num_B
elif giho == "/":
    resurt = num_A / num_B
elif giho == "*":
    resurt = num_A * num_B

print(f"= {num_A} {giho} {num_B} = {result}")