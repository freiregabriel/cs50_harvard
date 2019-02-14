def get_int(message):
    return int(input(message))
def get_float(message):
    return float(input(message))
    
# x = get_int("x: ")
# y = get_int("y: ")
x = get_float("x: ")
y = get_float("y: ")
print(f"x + y = {x + y:.2f}") # two decimal numbers
print(f"x - y = {x - y:.5f}") # five decimal numbers
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x mod y = {(x % y):.2f}")