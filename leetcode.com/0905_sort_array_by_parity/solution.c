int* sortArrayByParity(int* A, int ASize, int* returnSize)
{
    int* sorted = malloc(sizeof(int) * ASize);
    int begin = 0;
    int end = 0;
    
    for (auto int i = 0 ; i < ASize ; i++) {
        if (A[i] % 2 == 0 && end <= begin) {
            sorted[end++] = A[i];
            begin++;
        } else if (A[i] % 2 != 0) {
            sorted[end++] = A[i];
        } else {
            int tmp = sorted[begin];
            sorted[begin++] = A[i];
            sorted[end++] = tmp;
        }
    }
    
    *returnSize = ASize;
    return sorted;
}


