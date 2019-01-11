#include <stdio.h>

void cough(int n); // prototype declaration

int main(void) {
    cough(7);
}

void cough(int n) {
    for (int i = 0; i < n; i++) {
        printf("cough\n");
    }
}