#include <stdio.h>
#include <string.h>

int len(char s[]);
char* print_str(char s[]);
char* to_upper_case(char s[]);
char* to_lower_case(char s[]);

int main (void) {
    int arr[3];
    for (int i = 0; i < 3; i++) {
        arr[i] = (i + 1) * 2;
        printf("Iteration: %i; Value: %i\n", i, arr[i]);
    }
    char str[10];
    printf("String:\t");
    fgets(str, sizeof(str), stdin); /* Get a { string|char array } from user */
    printf("Lenght: %i\n", len(str));
    printf("Value: \t");
    print_str(str);
    char* upstr = to_upper_case(str);
    char* lowstr = to_lower_case(upstr);
    print_str(upstr);
    print_str(lowstr);
}
int to_ascii (char s) {
    return (int) s;
}
char* print_str(char s[]) {
    int n = len(s);
    for (int i = 0; i < n; i++) {
        printf("%c", s[i]);
    }
    printf("\n");
    return s;
}
char* to_upper_case(char s[]) {
    int n = len(s);
    char* s_temp;
    for (int i = 0; i < n; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s_temp[i] = s[i] - ('a' - 'A'); /* make letter uppercase */
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
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s_temp[i] = s[i] - ('A' - 'a'); /* make letter lowercase */
        } else {
            s_temp[i] = s[i];
        }
    }
    return s_temp;
}
int len(char s[]) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }
    return n;
}