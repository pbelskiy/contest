// Runtime: 0 ms, faster than 100.00% of Go online submissions for Sequential Digits.
// Memory Usage: 1.9 MB, less than 22.22% of Go online submissions for Sequential Digits.

var v = []int{
    12, 23, 34, 45, 56, 67, 78, 89,
    123, 234, 345, 456, 567, 678, 789,
    1234, 2345, 3456, 4567, 5678, 6789,
    12345, 23456, 34567, 45678, 56789,
    123456, 234567, 345678, 456789,
    1234567, 2345678, 3456789,
    12345678, 23456789, 123456789,
}

func sequentialDigits(low int, high int) []int {
    var r[]int

    for i := 0 ; i < len(v) ; i++ {
        if (v[i] >= low && v[i] <= high) {
            r = append(r, v[i])
        }
    }

    return r
}
