func tribonacci(n int) int {
    seq := [38]int{0,1,1}

    for i := 3 ; i <= n ; i++ {
        seq[i] = seq[i-1] + seq[i-2] + seq[i-3]
    }

    return seq[n]
}


