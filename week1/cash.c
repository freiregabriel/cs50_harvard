#include <stdio.h>
// 0.25
// 0.10
// 0.05
// 0.01
void cash(double change);
int main(void) {
    double n;
    printf("What's the change:\t");
    scanf("%lf", &n);
    printf("%f\n",n);
    cash(n);
}

void cash(double change) {
    double quarter = 0.25;
    double dime = 0.10;
    double nickel = 0.05;
    double penny = 0.01;
    double total = 0.0;
    int count = 0;
    double cChange = change;
    while (total < change) {
        if((quarter + total) <= change) {
            total += quarter;
            count++;
        } else if ((dime + total) <= change) {
            total += dime;
            count++;
        } else if ((nickel + total) <= change) {
            total += nickel;
            count++;
        } else if ((penny + total) <= change) {
            total += penny;
            count++;
        } else {
            break;
        }
    }
    printf("Number of coins used: %i\n", count);
    // printf("%f", change);
    printf("Total: %f", total);
}