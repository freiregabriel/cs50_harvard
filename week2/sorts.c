#include <stdio.h>
#include <string.h>
/**
 * Selection sort worst: On^2 best: On^2
 * Bubble sort worst: On^2 best: On
 * Insertion sort worst: On^2 best: O n
 * Merge sort worst: O n * log n best: O n * log n
 * 
 * Linear search worst: O n best: O1
 * Binary search worst: O log n best: O1 (ARRAY MUST BE SORTED)
 * 
 */
int LEN = 6;
void copy_array (int dest[], int src[]);
void bubble_sort(int a[], int size);
void insertion_sort (int a[], int size);
void print_array(int a[], int size);
int binary_search(int a[], int size, int target);
int linear_search(int a[], int size, int target);

int main(void) {
    int a[6] = {1, 5, 3, 4, 2, 6};
    insertion_sort(a, LEN);
    print_array(a, LEN);
    int c = binary_search(a, LEN, 5);
    int d = linear_search(a, LEN, 5);
    printf("Found on index: %d\n", c);
    printf("Found on index: %d\n", d);
}
void copy_array (int dest[], int src[]) {
    for (int i = 0; src[i]; i++) {
        dest[i] = src[i];
    }
}
void bubble_sort(int a[], int size) {
    int swapCounter = 0;
    // copy_array(b, a);
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (a[j] > a[i]) {
                int temp = a[j];
                a[j] = a[i];
                a[i] = temp;
                swapCounter++;
            }
        }
    }
    printf("Swapped %d times\n", swapCounter);
}
void insertion_sort (int a[], int size) {
    for (int i = 0; i < size; i++) {
        int sorted = a[i];
        int j = i - 1;
        while (j > -1 && a[j] > sorted) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = sorted;
    }
}
int linear_search(int a[], int size, int target) {
    int result = -1;
    for (int i = 0; i < size; i++) {
        if (a[i] == target) {
            result = i;
            break;
        }
    }
    return result;
}
int binary_search(int a[], int size, int target) {
    int result = 0;
    int start = 0;
    int end = size;
    int mid = (int) ( size / 2 ) * 1;
    while (size > 0) {
        if (mid < 0) {
            mid = 0;
        }
        if (a[mid] == target) {
            result = mid;
            break;
        }
        
        if (a[mid] > target) {
            // left
            size = mid;
            end = size - 1;
            mid = ((end + start) / 2) * 1;
        } else if (a[mid] < target) {
            // right
            start = mid + 1;
            size = end - start;
            mid = ((end + start) / 2) * 1;
        }
    }
    return result;
}
void print_array(int a[], int size) {
    int n = size;
    for(int i = 0; i < n; i++) {
        if (i < n - 1) {
            printf("%i, ", a[i]);
        } else {
            printf("%i", a[i]);
        }
    }
    printf("\n");
}