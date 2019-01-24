#include <stdio.h>

/*
    int: 4 bytes
    char: 1 byte
    float: 4 bytes
    double: 8 bytes
    long long: 8 bytes
    string|char*: 4 or 8 bytes 32 bits: 4 bytes 64 bits: 8 bytes

    memory is a big array of byte-sized cells
    arrays are pointers and don't get copied when passed as parameters to functions (in C)
*/
int main(void) {
    int k;
    k = 5;
    int* pk; /* declare a pointer pk (the value of a pointer is a memory address / the type describes the data located at that memory address) */
    pk = &k; /* pk is the address of k (where k lives in memory) */
    *pk = k; /* *pk is the value of k */
    printf("Memory address: %d\n", pk); /* print the address in memory */
    printf("Data Value: %d\n", *pk); /* print the value */
}