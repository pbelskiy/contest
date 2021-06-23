int subtractProductAndSum(int n)
{
    int s = 0;
    int p = 1;

    while (n > 0) {
        int d = n % 10;
        n /= 10;

        s += d;
        p *= d;
    }

    return p - s;
}