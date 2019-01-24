#include <stdio.h>
#include "credit.h"

void cp (FILE* source, FILE* target);
void cat (FILE* source);
/* 
    JPEG first 3 bytes: 0xff 0xd8 0xff
    check for JPEG:
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xE0) {
            // found JPEG
        }
    fopen(filepath, operation) ops: r/a/w
    fclose(file_pointer) close file using file_pointer
    fgetc(file_pointer) read first character of a file, file_pointer must be opened for "r": reading
    fputc(character, file_pointer) put character in a file. File must opened for "w": writing or "a" appending
    fread(<buffer>, <size>, <qty>, <file_pointer>) reads <qty> unitis of size <size> from the file pointed to and stores them in memory in a buffer
    fread is just a generic version of fgetc that allows to get any amount of information and store in memory
    
    //
    pseudocode for recover
    open card file
    repeat until end of card
        read 512 bytes into a buffer
        start of a new jpeg
            yes ->
            no ->
        already found a JPEG
            no ->
            yes ->
    close any remaining files
    //

    -- resize --
    biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + padding) * abs(bi.biHeight);
    bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    bi.biWidth *= n;
    bi.biHeight *= n;
    fseek(SEEK_CUR, SEEK_END, SEEK_STR)
*/
int main(void) {
    FILE* read = fopen("file1.txt", "r"); /* r: read a: append w:writing */
    FILE* tgt = fopen("file2.txt", "w"); /* r: read a: append w:writing */
    cat(read);
    FILE* read_again = fopen("file1.txt", "r"); /* r: read a: append w:writing */
    cp(read_again, tgt);
    /* 
    int arr[10];
    fread(arr, sizeof(int), 10, read); 

    -- dynamically allocating a buffer --
    double* arr2 = malloc(sizeof(double) * 80);
    fread(arr2, sizeof(double), 80, read);

     -- using variable --
     char c;
     fread(&c, sizeof(char), 1, ptr);
    */
}

void cp (FILE* source, FILE* target) {
    char ch;
    while((ch = fgetc(source)) != EOF) {
        fputc(ch, target);
    }
    fclose(source);
    fclose(target);
}
void cat (FILE* source) {
    char ch;
    while((ch = fgetc(source)) != EOF) {
        printf("%c", ch);
    }
    fclose(source);
}