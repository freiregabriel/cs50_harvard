#include <stdio.h>
#include <stdlib.h>

int HASH_MAX = 9;
unsigned int hash(char* str);

int main(void) {
    printf("%i\n", hash("Bart"));
}
unsigned int hash(char* str) {
    int sum = 0;
    for (int j = 0; str[j] != '\0'; j++) {
        sum += str[j];
    }
    return sum % HASH_MAX;
}