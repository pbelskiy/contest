func numSubarraysWithSum(nums []int, goal int) int {
    t := 0

    for i := 0 ; i < len(nums) ; i++ {
        s := 0
        for j := i ; j < len(nums) ; j++ {
            s += nums[j]
            if s == goal {
                t += 1
            }

            if s > goal {
                break
            }
        }
    }

    return t
}
