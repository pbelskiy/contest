func numSubarrayProductLessThanK(nums []int, k int) int {
    t := 0

    for i := 0 ; i < len(nums) ; i++ {
        p := 1
        for j := i ; j < len(nums) ; j++ {
            if (nums[j]*p < k) {
                p *= nums[j]
                t += 1
            } else {
                 break
            }
        }
    }

    return t
}
