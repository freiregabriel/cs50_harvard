#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "credit.h"
char* get_string(char* msg);
bool compare_strings(char* a, char* b);
int main(void) {
    char* str1 = get_string("String 1: ");
    if (str1 == NULL) {
        return 1;
    }
    char* str2 = get_string("String 2: ");
    if (str2 == NULL) {
        return 1;
    }
    printf("%s %d\n", str1, strlen(str1));
    printf("%s %d\n", str2, strlen(str2));
    printf("%d\n", compare_strings(str1, str2));
    printf("%d\n", strcmp(str1, str2));
    free(str1);
    free(str2);
    return 0;

}
char* get_string(char* msg) {
    char* str = malloc(100);
    printf("%s", msg);
    if (fgets(str, sizeof(str), stdin) && strlen(str) > 1) {
        return str;
    }
    return NULL;
}

bool compare_strings(char* a, char* b) {
    if (strlen(a) != strlen(b)) {
        return FALSE;
    }
    int n = strlen(a);
    for (int i = 0; i < n; i++) {
        if (a[i] != b[i]) {
            return FALSE;
        }
    }
    return TRUE;
}