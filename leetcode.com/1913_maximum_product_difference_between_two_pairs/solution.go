func maxProductDifference(nums []int) int {
    b1, b2 := 0, 0
    l1, l2 := math.MaxInt32, math.MaxInt32

    for _, n := range nums {
        if n >= b1 {
            b2 = b1
            b1 = n
        } else if n >= b2 {
            b2 = n
        }

        if n <= l1 {
            l2 = l1
            l1 = n
        } else if n <= l2 {
            l2 = n
        }
    }

    return b1*b2 - l1*l2
}
