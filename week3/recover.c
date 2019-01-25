#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 512

void recover_jpegs (FILE* image);

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: ./recover image\n");
        return 1;
    }
    char* name = argv[1];
    FILE* card = fopen(name, "r");
    if (card == NULL) {
        printf("Couldn't open file: %s\n", name);
        return 2;
    }

    recover_jpegs(card);

    // close file
    fclose(card);

    return 0;
}

/*
    Recover JPEG files from memory card
*/
void recover_jpegs (FILE* image) {
    // In signed char, the extended set takes value from -128 to -1 whereas in unsigned char it takes value from 128 to 255.
    unsigned char buffer[BUFFER_SIZE]; // i was getting Segmentation Fault error, fixed by using unsigned
    FILE* jpeg_f = NULL; // initialize every pointer as NULL, [DON'T FORGET]
    int found_jpeg = 0;
    int n_files = 0;
    // Notes: - the JPEG files are aligned one after the other
    //        - there are 4 standard bytes for JPEGs 0xFF 0xD8 0xFF and the fourth one is a bit harder so we use bitwise operator to compare binary digits
    //        - The & operator compares each binary digit of two integers and returns a new integer, with a 1 wherever both numbers had a 1 and a 0 anywhere else

    // read blocks of 512 bytes until there is no more bytes to read
    while (fread(buffer, BUFFER_SIZE, 1, image) == 1) {
        // check if it's a JPEG file
        if (buffer[0] == 0xFF &&
            buffer[1] == 0xD8 &&
            buffer[2] == 0xFF &&
            (buffer[3] & 0xFF) == 0xE0) {

            if (found_jpeg == 1) {
                // found another JPEG file, close previous one
                fclose(jpeg_f);
            } else {

                // jpeg file found, start writing
                found_jpeg = 1;

            }

            // create the file name
            char f_name[8];
            sprintf(f_name, "%03d.jpg", n_files);
            // create the file using the "append" mode
            jpeg_f = fopen(f_name, "a");
            n_files++;


        }

        if (found_jpeg == 1) {

            // write 512 bytes to file when we start finding JPEGs
            fwrite(&buffer, BUFFER_SIZE, 1, jpeg_f);

        }
    }
    // notify the user
    printf("found and recovered %d JPEG files\n", n_files);
    fclose(jpeg_f);
}