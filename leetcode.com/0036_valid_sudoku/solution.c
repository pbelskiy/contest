bool isValidSudoku(char** board, int boardSize, int* boardColSize)
{
    bool hor[9][9] = {false,};
    bool ver[9][9] = {false,};
    bool box[9][9] = {false,};

    for (int x = 0 ; x < 9 ; x++) {
        for (int y = 0 ; y < 9 ; y++) {
            if (board[x][y] == '.')
                continue;

            int val = board[x][y] - '0' - 1;
            int k = (x / 3) * 3 + (y / 3);

            if (hor[x][val] || ver[y][val] || box[k][val])
                return false;

            hor[x][val] = true;
            ver[y][val] = true;
            box[k][val] = true;
        }
    }

    return true;
}
