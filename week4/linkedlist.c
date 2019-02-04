#include <stdio.h>
#include <stdlib.h>
#include "sll.h"

sllnode* create(int val);
int find(sllnode* head, int val);
sllnode* insert(sllnode* head, int val);
void destroy(sllnode* head);
void print_llist(sllnode* head);

int main (void) {
    sllnode* list = create(4);
    printf("Created a list with head value: %i\n", list->number);
    list = insert(list, 3);
    printf("Insert a value to the list and now the head value is: %i, and next is:%i\n", list->number, list->next->number);
    list = insert(list, 5);
    printf("Insert a value to the list and now the head value is: %i, and next is:%i\n", list->number, list->next->number);
    list = insert(list, 6);
    printf("Insert a value to the list and now the head value is: %i, and next is:%i\n", list->number, list->next->number);
    printf("Does 3 exists? %i\n", find(list, 3));
    printf("Does 4 exists? %i\n", find(list, 4));
    printf("Does 5 exists? %i\n", find(list, 5));
    printf("Does 6 exists? %i\n", find(list, 6));
    printf("Does 7 exists? %i\n", find(list, 7));
    printf("Does 4 exists? %i\n", find(list, 4));
    printf("Does 8 exists? %i\n", find(list, 8));
    print_llist(list);
    destroy(list);
    printf("Destroyed list");
    // Node* numbers = NULL;
    // int size = 0;
    // while(1) {
    //     int number;
    //     printf("Number (type 0 to quit): "); 
    //     scanf("%d", &number);
    //     if (number == 0) {
    //         break;
    //     }
    //     Node* n = malloc(sizeof(Node));
    //     if (!n) {
    //         return 1;
    //     }
    //     n->number = number; // arrow notation < = > the same as < = > (*n).number (assessing the value, not the address, since n is a pointer) 
    //     n->next = NULL;
    //     if(numbers) {
    //         for (Node* ptr = numbers; ptr != NULL; ptr=ptr->next) {
    //             if (!ptr->next) { // found the end ?
    //                 ptr->next = n;
    //                 break;
    //             }
    //         }
    //         // or 
    //         // Node* ptr = numbers;
    //         // while (ptr != NULL) {
    //         //     if (!ptr->next) {
    //         //         ptr->next = n;
    //         //         break;
    //         //     }
    //         //     ptr = ptr->next;
    //         // }
    //     } else {
    //         numbers = n;
    //     }
    //     size++;
    // }
    // int i = 0;
    // Node* n = numbers;
    // while (n != NULL) {
    //     printf("value %i: %i\n", i + 1, n->number);
    //     n = n->next;
    //     i++;
    // }
}

sllnode* create(int val){
    sllnode* node = malloc(sizeof(sllnode));
    if (node != NULL) {
        node->number = val;
        node->next = NULL;
    }
    return node;
}

int find(sllnode* head, int val) {
    sllnode* curr = head;
    while(curr != NULL) {
        if (curr->number == val) {
            return 1;
        }
        if (!curr->next) {
            break;
        }
        curr = curr->next;
    }
    return 0;
}

sllnode* insert(sllnode* head, int val) {
    sllnode* new = malloc(sizeof(sllnode));
    new->number = val;
    new->next = head;
    return new;
}
void print_llist(sllnode* head) {
    sllnode* h = head;
    printf("List: [");
    while (h != NULL) {
        if (!h->next) {
            printf("%i", h->number);
            break;
        }
        printf("%i, ", h->number);
        h = h->next;
    }
    printf("]\n");
}
void destroy(sllnode* head) {
    sllnode* h = head;
    while(h->next != NULL) {
        sllnode* curr = h->next; 
        h->next = curr->next;
        free(curr);
    }
    free(h);
}