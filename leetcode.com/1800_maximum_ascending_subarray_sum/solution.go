func Max(a, b int) int {
    if a > b {
        return a
    }

    return b
}

func maxAscendingSum(nums []int) int {
    total := nums[0]
    max := nums[0]

    for i := 0 ; i < len(nums) ; i ++ {
        if i > 0 && nums[i] > nums[i - 1] {
            total += nums[i]
        } else {
            max = Max(max, total)
            total = nums[i]
        }
    }

    return Max(max, total)
}
