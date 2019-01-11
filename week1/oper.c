#include <stdio.h>
#include <string.h>

int main(void) {
    // string
    double x = 10;
    double y = 2;
    double z = y / x;
    char S[10];
    printf("Type a string:\t");
    scanf("%s", S);
    int l = strlen(S);
    printf("%i\n", l);
    printf("%f\n", x);
    printf("%.50f\n", x / 10.0);
    printf("%.50f\n", z);
    printf("%i\n", 20 % 4);
    printf("%i\n", 20 % 3);
    printf("%s\n", S);
    // end string
}
// the y 2k problem was that there was only 2 number showing year value 
// e.g. 1999 -> 99. So when the year turned 2000 it became -> 00, it could be interpreted as 1900 too