// #include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "credit.h"
bool valid(char* c);
int shift (char c);
void vigenere_cipher(char* text, char* keyword);

int main(int argc, char* argv[])
{
    char* keyword = argv[argc - 1];
    if (!valid(keyword) || argc > 2 || argc < 2) {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
    char inp[100];
    printf("plaintext: ");
    fgets(inp, sizeof(inp), stdin); /* Get a { string|char array } from user */
    // string inp = get_string("plaintext: ");
    printf("%s\n", inp);
    vigenere_cipher(inp, keyword);
    return 0;
}

int shift (char c) {
    int i = 0;
    if (isupper(c)) {
        i = c - 'A';
    } else if (islower(c)){
        i = c - 'a';
    }
    return i;
}
bool valid(char* c) {
    int i = 0;
    while(c[i] != '\0') {
        int d = c[i] -'0';
        if(d >= 0 && d <= 9){
            return FALSE;
        }
        i++;
    }
    return TRUE;
}
char cipher (char c, int k) {
    char a = c;
    if (isupper(a)) { // isalpha to know if it's a letter
        int asc = a - 'A';
        a = ((asc + k) % 26) + 'A';
    } else if (islower(a)) {
        int asc = a - 'a';
        a = ((asc + k) % 26) + 'a';
    }
    return a;
}
bool is_letter (char c) {
    return isupper(c) || islower(c);
}
void vigenere_cipher(char* text, char* keyword) {
    printf("ciphertext: ");
    int keyword_offset = 0;
    int i = 0;
    while(text[i] != '\0') {
        char curr_char = text[i];
        
        int idx = keyword_offset % strlen(keyword); /* [0 % 4 = 0], [1 % 4 = 1], [2 % 4 = 2], [3 % 4 = 3], [4 % 4 = 0], [5 % 4 = 1], [6 % 4 = 2] .... */
        char key_char = keyword[idx];
        
        /* old way */
        // char key_char = keyword[keyword_offset];
        // if (key_char == '\0') { /* check if it's the end of keyword */
        //     keyword_offset = 0; /* reset look up and get first char again */
        //     key_char = keyword[0];
        // }

        int k = shift(key_char); /* calculate shift for current keyword char */
        char chiphered_char = curr_char;
        if (isalpha(curr_char)) {
            chiphered_char = cipher(curr_char, k);
            keyword_offset++; /* initialize keyword look up */
        }

        /* old way */
        // if (is_letter(curr_char)) { /* check if the current input char is a letter */
        //     chiphered_char = cipher(curr_char, k); /* apply cipher operation */
        // } else {
        //     keyword_offset--; /* if not, use the same keyword char for the next word */
        // }
        
        printf("%c", chiphered_char);
        i++;
    }
    printf("\n");
}


/* PSEUDOCODE
 receive keyword as the second argument
    validate if the input received is a number
    validate if the user passed only one argument
    prompt user to get text to chipher
    for each character of the text
    add one to keyword offset lookup
    if character is a letter
        convert uppercase char to int
        get char from keyword
        check if it's the end of keyword
        if it is, reset the offset lookup
        get first keyword char
        calculate shift for current keyword char
        apply cipher operation to char
        convert int to char
    else if char is not a letter
        decrease one from the keyword offset lookup to use the same letter for the next iteration
  
  print the new character*/
 