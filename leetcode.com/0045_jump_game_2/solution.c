#define MAX 10000
#define MIN(a, b) (a < b ? a : b)

int *numbers;
int length;
int cache[MAX];

int dfs(int i)
{
    if (cache[i] != -1)
        return cache[i];

    if (i == length - 1)
        return 0;

    int r = INT_MAX;

    for (int j = i ; j < MIN(length - 1, i + numbers[i]) ; j++)
        r = MIN(r, dfs(j + 1) + 1);

    cache[i] = r;
    return r;
}

int jump(int *nums, int numsSize)
{
    numbers = nums;
    length = numsSize;
    memset(cache, -1, sizeof(int)*MAX);
    return dfs(0);
}
