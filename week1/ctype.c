#include <stdio.h>
#include <ctype.h>

char* to_upper_case(char s[]);
char* to_lower_case(char s[]);
char* print_str(char s[]);
/* 
    argv = argument vector 
    argc = argument count 
*/
int main(void) {
    char str[10];
    printf("String:\t");
    fgets(str, sizeof(str), stdin); /* Get a { string|char array } from user */
    char* upstr = to_upper_case(str);
    print_str(upstr);
    char* lowstr = to_lower_case(upstr);
    print_str(lowstr);
}
int len(char s[]) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }
    return n;
}
char* to_upper_case(char s[]) {
    int n = len(s);
    char* s_temp;
    for (int i = 0; i < n; i++) {
        if (islower(s[i])) {
            s_temp[i] = toupper(s[i]); /* make letter uppercase */
        } else {
            s_temp[i] = s[i];
        }
    }
    return s_temp;
}
char* to_lower_case(char s[]) {
    int n = len(s);
    char* s_temp;
    for (int i = 0; i < n; i++) {
        if (isupper(s[i])) {
            s_temp[i] = tolower(s[i]); /* make letter uppercase */
        } else {
            s_temp[i] = s[i];
        }
    }
    return s_temp;
}
char* print_str(char s[]) {
    int n = len(s);
    for (int i = 0; i < n; i++) {
        printf("%c", s[i]);
    }
    printf("\n");
    return s;
}
