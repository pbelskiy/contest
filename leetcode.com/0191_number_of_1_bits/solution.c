int hammingWeight(uint32_t n)
{
    int total = 0;

    for (int i = 0 ; i < 32 ; i++)
        total += ((uint32_t)1 << i & n) ? 1 : 0;

    return total;
}
