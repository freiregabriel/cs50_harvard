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
    int _orig_width = bi.biWidth;
    int _orig_height = bi.biHeight;
    
    bi.biWidth *= resize_num;
    bi.biHeight *= resize_num;
    
    int padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + padding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(_orig_height); i < biHeight; i++)
    {
        // iterate over pixels in scanline
        RGBTRIPLE triples[_orig_width];
        for (int j = 0; j < _orig_width; j++)
        {
            // temporary storage
            RGBTRIPLE triple;
            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
            triples[j] = triple;
        }
        for (int y = 0; y < resize_num; y++) {
            for (int j = 0; j < _orig_width; j++) {
                for(int x = 0; x < resize_num; x++) {
                    fwrite(&triples[j], sizeof(RGBTRIPLE), 1, outptr);
                }
            }
        }
        fseek(inptr, padding, SEEK_CUR);
        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outptr);
        }
    }
}
