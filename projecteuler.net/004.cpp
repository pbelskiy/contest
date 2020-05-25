#include <iostream>

using namespace std;

#define MAX_TEXT_LENGHT 1000
#define MAX_FIRST_NUM   999
#define MAX_SECOND_NUM  999

char text[MAX_TEXT_LENGHT];

int int2str(unsigned int n)
{
    /* clean */
    for (int i = 0 ; i < MAX_TEXT_LENGHT ; i++)
        text[i] = '\0';

    /* convert */
    int len = 0;
    while (n) {
        text[len++] = '0' + n % 10;
        n /= 10;
    }

    /* reverse */
    int i = 0;
    while (i < len / 2) {
        char tmp = text[len - i - 1];
        text[len - i - 1] = text[i];
        text[i] = tmp;
        i++;
    }

    return len;
}

bool is_polindrome(int len)
{
    int i = 0;

    while (i < len / 2) {

        if (text[len - i - 1] != text[i])
            return false;
        i++;
    }

    return true;
}

int main()
{
    int max = 0;

    for (int i = MAX_FIRST_NUM ; i > 0 ; i--) {
        for (int j = MAX_SECOND_NUM ; j > 0 ; j--) {

            int len = int2str(i * j);

            if (is_polindrome(len)) {
                if (i * j > max) max = i * j;
            }
        }
    }

    cout << max << endl;
    return 0;
}