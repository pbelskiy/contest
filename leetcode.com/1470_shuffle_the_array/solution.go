func shuffle(nums []int, n int) []int {
    a := make([]int, n*2)

    for i := 0 ; i < n ; i++ {
        a[i*2] = nums[i]
        a[i*2+1] = nums[n + i]
    }

    return a
}
