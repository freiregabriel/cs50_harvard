# from cs50 import get_int


def main():
    while True:
        n = input("Height: ")
        n = int(n)
        if n >= 1 and n < 9:
            break
    make_pyramid(n)

# Method to make a pyramid of height (n)


def make_pyramid(n):
    for i in range(n):
        # write the left half of the pyramid
        for j in reversed(range(n)):
            print(" " if j > i else "#", end="")
        
        # write two spaces
        print(" " * 2, end="")

        # write the right half of the pyramid
        for j in range(n):
            print("" if j > i else "#", end="")

        print()


main()
