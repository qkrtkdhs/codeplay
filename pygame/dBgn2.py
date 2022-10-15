question = 0
numbers = []
result = 0

while True:
    question = input("+-*/ : ")
    if "+" in question:
        numbers = question.split("+")
        result = int(numbers[0]) + int(numbers[1])
    elif "-" in question:
        numbers = question.split("-")
        result = int(numbers[0]) - int(numbers[1])
    elif "*" in question:
        numbers = question.split("*")
        result = int(numbers[0]) * int(numbers[1])
    elif "/" in question:
        numbers = question.split("/")
        result = int(numbers[0]) / int(numbers[1])
    elif "종료" in question:
        break
    print(f"{question} = {result}")
