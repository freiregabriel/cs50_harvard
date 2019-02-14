numbers = []
while True:
    number = input("Number: ")

    if not number:
        break
    number = int(number)
    if number not in numbers:
        numbers.append(number)

for number in numbers:
    print(number)