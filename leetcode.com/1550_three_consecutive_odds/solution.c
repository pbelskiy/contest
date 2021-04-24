bool threeConsecutiveOdds(int *arr, int arrSize)
{
    int count = 0;

    for (int i = 0 ; i < arrSize ; i++) {
        count = (arr[i] % 2 == 0) ? 0 : count + 1;
        if (count == 3)
            return true;
    }

    return false;
}
