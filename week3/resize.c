// Copies a BMP file

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

void resize(BITMAPFILEHEADER bf, BITMAPINFOHEADER bi, int resize_num, FILE* inptr, FILE* outptr);

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: n infile outfile\n");
        return 1;
    }

    // remember filenames
    int n = argv[1][0] - '0';
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // determine padding for scanlines
    resize(bf, bi, n, inptr, outptr);

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}

void resize(BITMAPFILEHEADER bf, BITMAPINFOHEADER bi, int resize_num, FILE* inptr, FILE* outptr) {
    BITMAPINFOHEADER bi_resized = bi;
    BITMAPFILEHEADER bf_resized = bf;

    bi_resized.biWidth *= resize_num;
    bi_resized.biHeight *= resize_num;

    int new_padding = (4 - (bi_resized.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    bi_resized.biSizeImage = ((sizeof(RGBTRIPLE) * bi_resized.biWidth) + new_padding) * abs(bi_resized.biHeight);
    bf_resized.bfSize = bf.bfSize - bi.biSizeImage + bi_resized.biSizeImage;

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf_resized, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&bi_resized, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    int biHeight = abs(bi.biHeight);
    int biWidth = abs(bi.biWidth);
    for (int i = 0; i < biHeight; i++)
    {
        // iterate over pixels in scanline
        for (int y = 0; y < resize_num; y++) {
            for (int j = 0; j < biWidth; j++) {
                // temporary storage
                RGBTRIPLE triple;
                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                // write <resize_num> x 2
                for(int x = 0; x < resize_num; x++)
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
            }
            for (int k = 0; k < new_padding; k++)
                fputc(0x00, outptr);

            if (y < resize_num - 1)
                fseek(inptr, -biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
        }
        // skip padding if any
        fseek(inptr, padding, SEEK_CUR);
    }
}
