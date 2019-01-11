#include <stdio.h>
#include <string.h>
#include "credit.h"

// input 4003600000000014
void validate(double n, int length);
int len (double n);

int main(void) {
    double n;
    do {
        printf("Number:\t");
        scanf("%lf", &n);
    } while (len(n) < 16 || len(n) > 16);
    // double n = get_long("Number:\t");
    int length = len(n);
    validate(n, length);
}
int len (double n) {
    int count = 0;
    long long temp_num = n;
    while (temp_num > 0LL) {
        temp_num = temp_num / 10LL;
        count++;
    }
    return count;
}
bool luhn_alg (double n, int length) {
    int sum = 0;
    long long t_num = n;
    for (int i = 1; i <= length; i++) {
        int digit = t_num % 10LL;
        // printf("%d\n", d);
        if (i % 2 == 0) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        t_num /= 10LL;
    }
    if (sum % 10 != 0) {
        return FALSE;
    }
    return TRUE;
}
void validate(double n, int length) {
    long long t_num = n;
    while (t_num > 100LL) {
        t_num /= 10LL;
    }
    int c_id = t_num;
    bool valid = luhn_alg(n, length);
    switch (c_id) {
        case 34:
        case 37:
            if (valid) {
                printf("AMEX\n");
            }
            break;
        case 51:
        case 52:
        case 53:
        case 54:
        case 55:
            if (valid) {
                printf("MASTERCARD\n");    
            }
            break;
        default:
            if ((c_id / 10 == 4) && valid) {
                printf("VISA\n");
            } else {
                printf("INVALID\n");
            }
    }
}
