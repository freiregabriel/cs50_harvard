import sys
s = input("Name: ")

def capitalize_first(string):
    # s1 = ""
    # for i, c in enumerate(string):
    #     if i == 0:
    #         c = c.upper()
    #     s1 += c
    # return s1
    return string[0].upper() + string[1:]
if len(sys.argv) >= 2:
    print(capitalize_first(sys.argv[1]))
if s != "":
    print(capitalize_first(s))

print(sys.argv)