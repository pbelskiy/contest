#include <stdio.h>
#include <string.h>

enum days {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
};

enum months {
    JANUARY,    // 31
    FEBRUARY,   // 28
    MARCH,      // 31
    APRIL,      // 30
    MAY,        // 31
    JUNE,       // 30
    JULY,       // 31
    AUGUST,     // 31
    SEPTEMBER,  // 30
    OCTOBER,    // 31
    NOVEMBER,   // 30
    DECEMBER    // 31
};


int year = 1901;
int date = 1;
int month = JANUARY;
int day = TUESDAY;

int sundays = 0;

void increase_date()
{
    if (day == TUESDAY && date == 15) sundays++;

    if (month == APRIL || month == JUNE || month == SEPTEMBER || month == NOVEMBER)
    {
        if (date == 30) {
            date = 1;
            month++;
        }
         else
        {
            date++;
        }
    }
     else if (month == FEBRUARY)
    {
        bool leap = (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;

        if ( (date == 28 && !leap) || (date == 29 && leap) )
        {
            date = 1;
            month++;
        } else date++;
    }
     else
    {
        if (date == 31)
        {
            month = (month == DECEMBER) ? JANUARY : month + 1;
            date = 1;

            if (date == 1 && month == JANUARY) year++;
        } else date++;
    }

    day = (day == SUNDAY) ? MONDAY : day + 1;
}

int main()
{
    while (year < 2222)
        increase_date();

    printf("\nsundays: %d\n", sundays);
    return 0;
}