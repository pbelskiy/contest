/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize,
                int* queriesColSize, int* returnSize)
{
    int *res = malloc(queriesSize * sizeof(int));

    for (int i = 0 ; i < queriesSize ; i++) {
        int v = 0;
        for (int j = queries[i][0] ; j <= queries[i][1] ; j++) {
            v ^= arr[j];
        }

        res[i] = v;
    }

    *returnSize = queriesSize;
    return res;
}
