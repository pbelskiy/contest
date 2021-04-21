int repeatedNTimes(int* A, int ASize)
{
    int freq[10000] = {0,};
    int n_freq = 0;
    int n_val = -1;

    for (int i = 0 ; i < ASize ; i++) {
        freq[A[i]]++;

        if (freq[A[i]] > n_freq) {
            n_freq = freq[A[i]];
            n_val = A[i];
        }
    }

    return n_val;
}


