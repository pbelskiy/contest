int tribonacci(int n)
{
    int seq[38] = {0, 1, 1, };

    for (int i = 3 ; i <= n ; i++) {
        seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3];
    }

    return seq[n];
}