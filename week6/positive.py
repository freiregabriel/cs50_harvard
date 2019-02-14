def main():
    i = get_positive_int("Positive integer: ")
    print(i)

def get_positive_int(message):
    while True:
        n = int(input(message))
        if n > 0:
            break
    return n
if __name__ == "__main__":
    main()