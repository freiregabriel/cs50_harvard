#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "credit.h"
string get_string(string msg);
bool string_equals(string a, string b);
int main(void) {
    string str1 = get_string("String 1: ");
    if (str1 == NULL) {
        return 1;
    }
    string str2 = get_string("String 2: ");
    if (str2 == NULL) {
        return 1;
    }
    printf("%s %d\n", str1, strlen(str1));
    printf("%s %d\n", str2, strlen(str2));
    printf("%d\n", string_equals(str1, str2));
    printf("%d\n", strcmp(str1, str2));
    free(str1);
    free(str2);
    return 0;

}
string get_string(string msg) {
    string str = malloc(100 * sizeof(char));
    printf("%s", msg);
    if (fgets(str, sizeof(str), stdin) && strlen(str) > 1) {
        string copy = str;
        return copy;
    }
    return NULL;
}

bool string_equals(string a, string b) {
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