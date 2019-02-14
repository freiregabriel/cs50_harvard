from cs50 import get_string


def main():
    # get input from user
    while True:
        try:
            n = get_string("Number: ")
            num = int(n)
            if type(num) == int:
                break
        except ValueError:
            pass
    # validate
    validate(n)


def luhn_alg(n):
    sum = 0
    # traverse the card num 2 digits at a time and perform luhn algorithm
    for i in range(len(n)):
        digit = int(n[i: i + 2])
        if (i+1) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit  # calculate sum
    return sum % 10 != 0


def validate(n):
    # get first 2 digits
    digits = int(n[:2])
    # validate using luhn algorithm
    valid = luhn_alg(n)

    # check first two digits and print result
    if (digits == 37 or digits == 34) and valid:
        print("AMEX")
    elif (digits >= 51 and digits <= 55) and valid:
        print("MASTERCARD")
    elif int(digits / 10) == 4 and valid:
        print("VISA")
    else:
        print("INVALID")


main()