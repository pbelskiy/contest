int minimumMoves(char *s)
{
    int moves = 0;

    for (int i = 0 ; i < strlen(s) ; i++) {
        if (s[i] == 'O')
            continue;

        moves++;
        i += 2;
    }

    return moves;
}
