from cs50 import get_string
from sys import argv


def main():
    # validate usage
    if len(argv) != 2:
        print("Usage: python banned.py dictionary")
        exit(1)

    # get user input
    text = get_string("What message would you like to censor?\n")
    file_name = argv[1]
    # open file
    words_list_file = open(file_name, "r")
    # execute censoring task
    censored_text = censor(text, words_list_file)
    # display to the user
    print(censored_text)
    # close the file
    words_list_file.close()


def censor(text, file):
    # store user input words
    words = [w for w in text.split(" ")]
    # traverse the file
    for line in file:
        # store two versions of the banned word, lower case and upper case
        line_word_l = line.rstrip("\n").lower()
        line_word_u = line.rstrip("\n").upper()
        # check wether this is a banned word and replace with stars *
        if line_word_l in words:
            idx = words.index(line_word_l)
            words[idx] = ''.join(["*" for i in range(len(line_word_l))])
        elif line_word_u in words:
            idx = words.index(line_word_u)
            words[idx] = ''.join(["*" for i in range(len(line_word_u))])
    # return the new text
    return ' '.join(words)


if __name__ == "__main__":
    main()
