#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int len(string s);
void caesar_cipher(string text, int k, int n);
bool valid(string c);

int main(int argc, string argv[])
{
    string c = argv[argc - 1];
    if (!valid(c) || argc > 2) {
        printf("Usage: ./caesar key\n");
        return 0;
    }
    int k = atoi(c);
    string inp = get_string("plaintext: ");
    int n = len(inp);
    caesar_cipher(inp, k, n);
}
bool valid(string c) {
    int n = len(c);
    for(int i = 0; i < n; i++) {
        int d = c[i] -'0';
        if(d < 0 || d > 9){
            return false;
        }
    }
    return true;
}
int len(string s) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }
    return n;
}
char cipher (char c, int k) {
    char a = c;
    if (isupper(a)) {
        int asc = a - 'A';
        a = ((asc + k) % 26) + 'A';
    } else if (islower(a)) {
        int asc = a - 'a';
        a = ((asc + k) % 26) + 'a';
    }
    return a;
}
void caesar_cipher(string text, int k, int n) {
    printf("ciphertext: ");
    for(int i = 0; i < n; i++) {
        char curr_char = text[i];
        char chiphered_char = cipher(curr_char, k);
        printf("%c", chiphered_char);
    }
    printf("\n");
}
/**
 * PSEUDOCODE
 * receive number as the second argument
validate if the input received is a number
validate if the user passed only one argument
prompt user to get text to chipher
for each character of the text
  if character is uppercase
    convert uppercase char to int
    apply cipher operation to uppercase char
    convert int to uppercase char
  else if char is lowercase
    convert lowercase char to int
    apply cipher operation to lowercase char
    convert int to lowercase char
  
  print the new character
*/
