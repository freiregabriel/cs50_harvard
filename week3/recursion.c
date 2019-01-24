#include <stdio.h>
/*
    recursion is basically a function that calls it self making the problem a bit smaller somehow
*/

int factorial(int n);
int sum (int* arr, int s, int idx);

int main(void) {
    int i[5] = { 1, 2, 3, 4, 10 };
    printf("%d\n", factorial(4));
    printf("%d\n", sum(i, 0, 4));
}

int factorial(int n) {
    if (n == 1)  /* base case */
        return n;
     else 
        return n * factorial(n - 1); /*  recursive case */
}
int sum (int* arr, int s, int idx) {
    if (idx < 0) { /* base case */
        return s;
    }
    s += arr[idx];
    return sum(arr, s, idx-1); /* recursive case */
}