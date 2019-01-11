#include <stdio.h>
void drawPyramid(int height);
int main(void)
{
    int height;
    do {
        printf("Height:\t");
        scanf("%d",&height);
    } while (height < 1 || height > 8);
    drawPyramid(height);
}
// Draw space or hash
void drawCell (int idx, int row) {
    if (idx > row) {
        printf(" ");
    } else {
        printf("#");
    }
}
// Draw gap of size {size}
void drawGap (int size) {
    for (int i = 0; i < size; i++) {
        printf(" ");
    }
}
// Draw N lef and right rows with Y of gap size in between
void drawRows (int n, int y) {
    for (int x = 1; x <= n; x++) {
        // left 
        for(int i = n; i >= 1; i--) {
            drawCell(i, x);
        }
        // spaces
        drawGap(y);
        // right
        for(int i = 1; i <= n; i++) {
            drawCell(i, x);
        }
        if (x != n) {
            printf("\n");
        }
    }
}
void drawPyramid(int height) {
    int spaces = 2;
    drawRows(height, spaces);
}
