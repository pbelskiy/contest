#include <stdio.h>

int main()
{
    int target  = 200;
    int ways = 0;

    for (int a = target; a >= 0; a -= 200) {
        for (int b = a; b >= 0; b -= 100) {
            for (int c = b; c >= 0; c -= 50) {
                for (int d = c; d >= 0; d -= 20) {
                    for (int e = d; e >= 0; e -= 10) {
                        for (int f = e; f >= 0; f -= 5) {
                            for (int g = f; g >= 0; g -= 2) {
                                ways++;
                            }
                        }
                    }
                }
            }
        }
    }

    printf("%d\n", ways);
    return 0;
}