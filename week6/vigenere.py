# from cs50 import get_string
from sys import argv


def main():

    # validate user input
    if len(argv) != 2 or not is_valid_keyword(argv[1]):
        print("Usage: python vigenere.py K")
        exit(1)

    keyword = argv[1]
    # get input from user
    plain_text = input("plaintext: ")
    # get ciphered text and display to the user
    ciphered_text = vigenere_cipher(plain_text, keyword)
    print(f"ciphertext: {ciphered_text}")


# Vigenere algorithm

def vigenere_cipher(text, keyword):
    keyword_offset = 0  # index of keyword
    ciph = ""
    key_length = len(keyword)
    for char in text:
        # check if current char is alpha
        if not char.isalpha():
            ciph += char
            continue
        # apply cipher algorithm to alpha character
        keyword_idx = keyword_offset % key_length
        ciph += cipher_char(char, keyword[keyword_idx])
        # increase index
        keyword_offset += 1

    return ciph


# Cipher plain text character using key character

def cipher_char(word_char, key_char):
    # get char ASCII values
    c, offset = to_ascii(word_char)
    k, _ = to_ascii(key_char)
    # apply cipher formula
    asc = (c + k) % 26
    # generate char using offset
    res = chr(asc + offset)
    return res.lower() if word_char.islower() else res.upper()


# Method to get ASCII character

def to_ascii(char):
    # offset to treat every character from 0 to 25 index
    offset = 65 if char.isupper() else 97
    c = ord(char) - offset
    return c, offset


def is_valid_keyword(keyword):
    # check every character and validate
    # if there are digits the keyword is invalid
    for c in keyword:
        if c.isdigit():
            return False
    return True


main()