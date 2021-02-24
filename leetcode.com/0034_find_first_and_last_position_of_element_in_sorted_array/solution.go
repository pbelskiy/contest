func searchRange(nums []int, target int) []int {
    result := []int{-1,-1}

    for i, n := range nums {
        if n == target {
            result[0] = i
            result[1] = i

            for j := i + 1 ; j < len(nums) ; j++ {
                if nums[j] != target {
                    break
                }

                result[1] = j
            }

            break
        }
    }

    return result
}
