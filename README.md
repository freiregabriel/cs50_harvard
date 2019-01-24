# Harvard CS50x edx
Notes for CS50x Introduction to Computer Science.
## Week 1
### Compilation

**C** *>* **Assembly** *>* **010100011100** (binary read by the CPU)

### UNIX Commands
- `ls` list directories 
- `mkdir directoryname` make a new directory 
- `cp src.txt trgt.txt` copy file 
- `cp -r src trgt` copy directory. The `-r` stands for recursive
- `rm -f file.txt` remove file  
- `rm -r directory` remove directory
- `rm -rf directory` combine `-f` and `-r`

### C DataTypes and Variables
- `int ` Integer 4 bytes of memory(32 bits)
- `unsigned int ` Use unsigned if you know your value will never be negative.
- `char ` char data type stores single characters (8 bits|1 byte)
- `float` for storing floating-point numbers with decimal part that takes 4 bytes of memory (32 bits|4 bytes)
- `double` for storing floating-point numbers with decimal part that takes 8 bytes of memory (64 bits|8 bytes) [Double precision]
- `void` is not a data type, it's a type. it is a placeholder for "nothing"
- `struct` structures
- `typedefs` for creating custom data types

```c
    int number; // declaration
    number = 17; // assignment
    char letter; // declaration
    letter = 'H'; // assignment
    int x = 17; // initialization
    char y = 'X'; // initialization
```
> Included in <cs50.h>
- `bool` true or false values / 1 and 0.
- `string` string data type == array of characters `char str[size]`.
- `int x;` integer variable
- `x` x variable
- `&x` address of x

### Loops in C
while loop
```c
while(true) {
    // will execute forever
}
```
do-while loop
```c
int n = 0;
do {
    // will at least once and until user types n >= 1
    n = prompt();
} while (n < 1);
```
for loop
```c
int n = 10;
for(int i = 0; i < n; i++) { // for(start; expression; increment)
    printf("Hello %i", i); // will print "Hello {i}" ten times
}
```
### Operators
- `=` Assign value to a variable
- `+` Add
- `-` Subtract
- `*` Multiply
- `/` Devide
- `%` Mod
```c
int y = 1;
int x = y + 1; // 2
int z = x + y; // 3
int z1 = x % y // 0
int z2 = z % x // 1
// mult
x = x * 5;
x *= 5;
// add
x = x + 1;
x += 1;
x++;
// sub
x = x - 1;
x -= 1;
x--;
if (x > y) {
    // x is greater than y
} else if (x <= y){
    // x is less or equal than y
}
if (z % y == 0) {
    // do something
} else if (z % y == 1) {
    // do something else
}
bool x = true;
bool y = true;
if (x && y) {
    // x and y are true
} else {
    // one of them is false
}
if (!x) {
    // x is false
}
if (x == y) {
    // x is equals to y
}
if (x != y) {
    // x is not equals to y
}
```
### Sort algorithms
```c
/**
 * Selection sort worst case: On^2 best case: On^2
 * Bubble sort worst case: On^2 best case: On
 * Insertion sort worst case: On^2 best case: O n
 * Merge sort worst case: O n * log n best case: O n * log n
 * 
 * Linear search worst case: O n best case: O1
 * Binary search worst case: O log n best case: O1 (ARRAY MUST BE SORTED)
 */
```

### Pointers
```c
/*
    int: 4 bytes
    char: 1 byte
    float: 4 bytes
    double: 8 bytes
    long long: 8 bytes
    string: ??? bytes

    memory is a big array of byte-sized cells
    arrays are pointers and don't get copied when passed as parameters to functions (in C)
*/
int main(void) {
    int k;
    k = 5;
    int* pk; /* declare a pointer pk (the value of a pointer is a memory address / the type describes the data located at that memory address) */
    pk = &k; /* pk is the address of k (where k lives in memory) */
    printf("Memory address: %d\n", pk); /* print the address in memory */
    printf("Data Value: %d\n", *pk); /* print the value */
}
```