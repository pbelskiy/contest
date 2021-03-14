func check(nums []int) bool {
    bp := 0

    for i := 0 ; i < len(nums) ; i++ {
        if nums[i] > nums[(i + 1) % len(nums)] {
            bp++
        }
    }

    if bp > 1 {
        return false
    }

    return true
}