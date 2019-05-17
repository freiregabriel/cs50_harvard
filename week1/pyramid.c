#include <cs50.h>
#include <stdio.h>


void draw_pyramid(int height);


int main(void)
{
    int height;
    do
    {
        // get input from user
        height = get_int("Height:\t");
    }
    while (height < 1 || height > 8);
    
    // draw a pyramid
    draw_pyramid(height);
}


// Draw a cell containing spaces or hashs
void draw_cell(int idx, int row)
{
    if (idx > row)
    {
        printf(" ");
    }
    else
    {
        printf("#");
    }
}


// draw a pyramid of a specific height
void draw_pyramid(int height)
{
    // draw rows
    for (int x = 1; x <= height; x++)
    {
        // left
        for (int i = height; i >= 1; i--)
        {
            draw_cell(i, x);
        }
        printf(" ");
        // right
        for (int i = 1; i <= height; i++)
        {
            draw_cell(i, x);
        }
        printf("\n");
    }
}
