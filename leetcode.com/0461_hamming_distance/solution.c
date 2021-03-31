int hammingDistance(int x, int y)
{
    int diff_count = 0;

    for (int shift = 0 ; shift < sizeof(int)*8 ; shift++)
        if ((((unsigned int)x >> shift) & 1) != (((unsigned int)y >> shift) & 1))
            diff_count++;

    return diff_count;
}
