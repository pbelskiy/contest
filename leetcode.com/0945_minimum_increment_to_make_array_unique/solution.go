func minIncrementForUnique(nums []int) int {
    sort.Ints(nums)

    total := 0

    for i := 0 ; i < len(nums) - 1 ; i++ {
        if (nums[i] < nums[i + 1]) {
            continue
        }

        d := nums[i] - nums[i + 1] + 1
        total += d
        nums[i + 1] += d
    }

    return total
}
