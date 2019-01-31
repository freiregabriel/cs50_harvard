#include <stdio.h>
#include <stdlib.h>
#include "struct.h"

int main (void) {
    Node* numbers = NULL;
    int size = 0;
    while(1) {
        int number;
        printf("Number (type 0 to quit): "); 
        scanf("%d", &number);
        if (number == 0) {
            break;
        }
        Node* n = malloc(sizeof(Node));
        if (!n) {
            return 1;
        }
        n->number = number; // arrow notation < = > the same as < = > (*n).number (assessing the value, not the address, since n is a pointer) 
        n->next = NULL;
        if(numbers) {
            for (Node* ptr = numbers; ptr != NULL; ptr=ptr->next) {
                if (!ptr->next) { // found the end ?
                    ptr->next = n;
                    break;
                }
            }
            // or 
            // Node* ptr = numbers;
            // while (ptr != NULL) {
            //     if (!ptr->next) {
            //         ptr->next = n;
            //         break;
            //     }
            //     ptr = ptr->next;
            // }
        } else {
            numbers = n;
        }
        size++;
    }
    int i = 0;
    Node* n = numbers;
    while (n != NULL) {
        printf("value %i: %i\n", i + 1, n->number);
        n = n->next;
        i++;
    }
}