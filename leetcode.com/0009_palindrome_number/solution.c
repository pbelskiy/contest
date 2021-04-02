#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x)
{
    if (x < 0)
        return false;

    char s[sizeof(int)*8+1] = {0,};
    int len = 0;

    while (x != 0) {
        s[len++] = x % 10 + '0';
        x /= 10;
    }

    for (int i = 0 ; i < len / 2 ; i++) {
        if (s[i] != s[len - 1 - i])
            return false;
    }

    return true;
}

int main()
{
    printf("%d == 1\n", isPalindrome(54145));
    printf("%d == 1\n", isPalindrome(111));
    printf("%d == 0\n", isPalindrome(102));
    printf("%d == 0\n", isPalindrome(-101));
    return 0;
}