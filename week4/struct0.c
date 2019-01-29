#include "struct.h"
#include <stdlib.h>
#include <stdio.h>

int main(void) {
    int enrollment;
    printf("Enrollment: "); 
    scanf("%d", &enrollment);
    student students[enrollment];
    for (int i = 0; i < enrollment; i++) {
        students[i].name = "Gabriel";
        students[i].dorm = "01";
        printf("name: %s; dorm:%s\n", students[i].name, students[i].dorm);
    }

}