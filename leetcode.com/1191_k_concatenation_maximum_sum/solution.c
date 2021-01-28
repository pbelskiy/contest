#include <stdio.h>

#define MAX(a, b) (a > b) ? a : b

int kConcatenationMaxSum(int* arr, int arrSize, int k)
{
    long long lmax = 0;
    long long gmax = 0;

    for (int i = 0 ; i < k ; i++) {
        for (int j = 0 ; j < arrSize ; j++) {
            lmax = MAX(arr[j], arr[j] + lmax);

            if (lmax > gmax)
                gmax = lmax;
        }
    }

    return gmax % 1000000007;
}

int main()
{
    int arr[] = {10000,10000,10000,10000,10000,10000,10000,10000,10000,10000};
    int k = 100000;

    printf("%d\n", kConcatenationMaxSum(arr, sizeof(arr) / sizeof(int), k));
}
