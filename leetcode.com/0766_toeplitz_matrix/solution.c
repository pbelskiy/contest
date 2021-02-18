bool isToeplitzMatrix(int** matrix, int matrixSize, int* matrixColSize)
{
    for (int y = 1 ; y < matrixSize ; y++) {
        for (int x = 1 ; x < *matrixColSize ; x++) {
            if (matrix[y][x] != matrix[y-1][x-1])
                return false;
        }
    }

    return true;
}
