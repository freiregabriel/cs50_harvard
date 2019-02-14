def get_int(message):
    return int(input(message))

x = get_int("x: ")
y = get_int("y: ")

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is lesser than y")
else:
    print("x is equal to y")
