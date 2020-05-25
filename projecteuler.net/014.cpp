#include <stdio.h>
#include <string.h>

int main()
{
    unsigned long n = 0, l = 0;

    for (unsigned long i = 1 ; i < 1000000 ; i++) {

        unsigned long cn = i;
        unsigned long cl = 0;

        while (cn > 1) {
            if (cn % 2 == 0) {
                cn /= 2;
                cl++;
            } else {
                cn = 3 * cn + 1;
                cl++;
            }
        }

        if (cl > l) {
            l = cl;
            n = i;
        }
    }

    printf("%lu\n", n);
    return 0;
}

