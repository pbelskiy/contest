
#include <stdio.h>

int get_factors_count(unsigned long num) {
    unsigned long start = 2;
    int factors_count = 1, i;

    while (num != 1) {
        i = 0;
        while (num % start == 0) {
            num /= start, i++;
        }
        factors_count *= i + 1;
        start++;
    }
    return factors_count;
}


int main() {
    int i;
    unsigned long num;

    for (num=0,i=1;;i++) {
        num += i;
        if (get_factors_count(num) > 1000) {
            printf("%ld", num);
            break;
        }
    }

    return 0;
}

