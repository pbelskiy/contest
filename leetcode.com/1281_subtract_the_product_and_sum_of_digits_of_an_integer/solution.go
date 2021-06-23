func subtractProductAndSum(n int) int {
    p, s := 1, 0

    for n > 0 {
        d := n % 10
        n /= 10
        p *= d
        s += d
    }

    return p - s
}