def main():
    cough(3)

def cough(n: int):
    if type(n) != int:
        print("Usage: cough(n: int)")
    for i in range(n):
        print("cough")

if __name__ == "__main__":
    main()