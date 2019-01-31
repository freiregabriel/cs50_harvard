#include <stdio.h>
#include <stdlib.h>
#include "struct.h"

int main (void) {
    int capacity = 0;
    // do {
    //     printf("Capacity: ");
    //     scanf("%i", &capacity);
    // } while (capacity < 1);
    // int numbers[capacity];
    int* numbers = NULL;
    int size = 0;
    while (1) {
        int number;
        printf("Number (type 0 to quit): "); 
        scanf("%d", &number);
        if (number == 0) {
            break;
        }
        if (size == capacity) {
            int* tmp = realloc(numbers, sizeof(int) * (size + 1)); // reallocate more memory to increase the size of array
            if (tmp == NULL) {
                // quit
                return 0;
            }
            numbers = tmp;
        }
        numbers[size] = number;
        size++;
        capacity++;
    }
    printf("You inputted the array: ");
    printf("[ ");
    for (int i = 0; i < size; i++) {
        if (i < size - 1) {
            printf(" %i, ", numbers[i]);
        } else {
            printf(" %i", numbers[i]);
        }
    }
        printf(" ]");
    free(numbers);
}