#define _XOPEN_SOURCE

#include <cs50.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

static const char alphabet[] =
"abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"0123456789";
static const int alphabetSize = sizeof(alphabet) - 1;
void brute_force(int maxLen, char* hash);

int main(int argc, string argv[])
{
    if (argc != 2) {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    string hash = argv[argc - 1];
    brute_force(5, hash);
    return 0;
}


bool generate_and_compare(char* result_string, char* hash, char* salt, int index, int maxDepth){
    bool found = false;
    for (int i = 0; i < alphabetSize; ++i) {
        result_string[index] = alphabet[i];
        if (index == maxDepth - 1) { /* finished creating word with maxDepth characters */
            if (!strcmp(hash, crypt(result_string, salt))) { /* Check hashes */
                printf("%s\n", result_string); /* print result and end recursion */
                found = true;
                return found;
            }
        }
        else {
            found = generate_and_compare(result_string, hash, salt, index + 1, maxDepth);
        }
        if (found) {
            break; /* leave loop */
        }
    }
    return found;
}

void brute_force(int maxLen, char* hash) {
    string result_string = malloc(maxLen + 1); /* previously allocate memory for string buffer */
    char salt[2] = { hash[0], hash[1] }; /* Create hash salt from 2 first characters */
    bool found = false;
    for (int i = 1; i <= maxLen; ++i) {
        memset(result_string, 0, maxLen + 1);
        /* Generate random words using alphabet and compare hashes */
        found = generate_and_compare(result_string, hash, salt, 0, i); 
        if (found) {
            break;
        }
    }

    free(result_string);
}

/**
 * 
 * PSEUDOCODE
 * 
 * we need a char array of the alphabet
get the hash from user
validate arguments
  exit with 1 if more than one or no argument
perform bruteforce to break the hash into a password
  use the alphabet to generate words from 1 to 5 of length
  for each length from 1 to maxLength => (5)
    generate word
      for each alphabet letter
        add a character to a new string
        if string reached the desired length
          check if the encrypted hashed result matches the target one
          if yes 
            you found the password 
            print password
            end program
        if not
          repeat the process, maybe using some kind of recursion until the string is complete
        

 * /