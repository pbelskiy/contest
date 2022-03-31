func minimumMoves(s string) int {
    moves := 0

    for i := 0 ; i < len(s) ; i++ {
        if (s[i] == 'X') {
            moves += 1
            i += 2
        }
    }

    return moves
}
