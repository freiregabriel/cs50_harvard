#include <stdio.h>
#include "credit.h"

float mult_float(float a, float b);
bool valid_triangle (int a, int b, int c);

int main(void) {
    float x;
    float y;
    do {
        printf("Number 1:\t");
        scanf("%f", &x);
    } while (!x);
    printf("Number 2:\t");
    scanf("%f", &y);
    float result = mult_float(x, y);
    printf("Result: %f\n", result);
    printf("Valid? %d\n", valid_triangle(5, 5, 5));
}
float mult_float(float a, float b) {
    return a * b;
}
bool valid_triangle (int a, int b, int c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return FALSE;
    } else if ((a + b) <= c && (a + c) <= b && (b + c) <= a) {
        return FALSE;
    }
    return TRUE;
}