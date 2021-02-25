bool lemonadeChange(int *bills, int billsSize)
{
    int total_five = 0;
    int total_ten = 0;

    for (int i = 0 ; i < billsSize ; i++) {
        switch (bills[i]) {
        case 5:
            total_five += 1;
            continue;

        case 10:
            if (total_five == 0)
                return false;

            total_ten += 1;
            total_five -= 1;
            continue;

        case 20:
            if (total_ten > 0 && total_five > 0) {
                total_ten -= 1;
                total_five -= 1;
                continue;
            }

            if (total_five < 3)
                return false;
   
            total_five -= 3;
            continue;
        }
    }

    return true;
}
