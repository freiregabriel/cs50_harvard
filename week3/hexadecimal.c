#include <stdio.h>

/*
    decimal system: 0 1 2 3 4 5 6 7 8 9
    binary system: 0 1
    hexadecimal system: 0 1 2 3 4 5 6 7 8 9 A B C D E F (16 is power of 2, so each digit corresponds to an arrengement of 4 bits) easy to express complex numbers
    0x0 0x1 0x2 0x3 0x4 0x5 0x6 0x7 0x8 0x9 0xA 0xB 0xC 0xD 0xF
    1: 0000
    2: 0001
    3: 0010
    0x397 : 256 16 1 | 16^2 16^1 16^0 > (3 * 16^2) + (9 * 16) + (7) > 768 + 144 + 7 = 919
    0xADC : 256 16 1 | 16^2 16^1 16^0 > (10 * 16^2) + (13 * 16) + (12) > 2560 + 208 + 12 = 2780
    hexadecimals are not used for MATH, but to refer to memory location as it is done in C
*/
int main(void) {
    int num1 = 0x397;
    int num2 = 0xADC;
    printf("%d\n", num1);
    printf("%d\n", num2);
}