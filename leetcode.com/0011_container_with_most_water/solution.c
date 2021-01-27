#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))

int maxArea(int* height, int heightSize)
{
    int result = 0;
    int begin = 0;
    int end = heightSize - 1;

    while (begin < end) {
        int square = (end - begin) * MIN(height[begin], height[end]);

        if (square > result)
            result = square;

        if (height[begin] < height[end]) {
            begin++;
        } else {
            end--;
        }
    }

    return result;
}

int main()
{
    int size = 15000;
    int* height = malloc(sizeof(int) * size);

    for (int i = 0 ; i < size ; i++)
        height[i] = rand() % 1000;

    printf("%d == 14743480\n", maxArea(height, size));
    return 0;
}
