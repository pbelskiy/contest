#include <stdio.h>
#include <string.h>

#define MAX_LEN 1000

const char *basic[21] = {
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
};

const char *basic2[10] = {
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
};

char speech[MAX_LEN];

int convert_to_speech(unsigned int n)
{
    if (n <= 20) {
        strcpy(speech, (char*) basic[n]);
    }

    else if (n < 100) {
        sprintf(speech, "%s%s", (char*) basic2[n / 10], (char*) basic[n % 10]);
    }

    else if (n < 1000) {
        int p = sprintf(speech, "%shundred", (char*) basic[n / 100]);

        if (n % 100 != 0) {
            n = n % 100;

            if (n <= 20) {
                sprintf(&speech[p], "and%s", (char*) basic[n]);
            } else {
                sprintf(&speech[p], "and%s%s", (char*) basic2[n / 10],
                                               (char*) basic[n % 10]);
            }
        }
    }

    else if (n == 1000) {
        sprintf(speech, "onethousand");
    }

    // printf("%lu - %s\n", strlen(speech), speech);
    return strlen(speech);
}

int main()
{
    int len = 0;

    for (int i = 1 ; i <= 1000; i++)
        len += convert_to_speech(i);

    printf("%d\n", len);
    return 0;
}