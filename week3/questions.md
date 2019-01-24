# Questions

## What's `stdint.h`?

It's a header file from the C standard library to allow programmers to write more portable code
by providing a set of typedefs that specify exact-width integer types.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

To write more portable code, it is particularly useful for embedded programming which often involves considerable manipulation of hardware specific I/O registers requiring integer data of fixed widths, specific locations and exact alignments.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

- BYTE is 1 byte
- DWORD is 4 bytes
- LONG is 4 bytes
- WORD is 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

0x42 and 0x4D

## What's the difference between `bfSize` and `biSize`?

bfSize is in bytes of the bitmap file and biSize is the number of bytes required by the structure

## What does it mean if `biHeight` is negative?

if biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

in line 24 could be because the file does not exist
and in line 32 could be because there is no sufficient memory to write the data into the file or a permission issue, or a badly formatted file name.

## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

because we are writing one element of size `<size>` at a time

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

sets the file position of the stream to the given offset

## What is `SEEK_CUR`?

sets the file position of the stream to the given offset from the current position
