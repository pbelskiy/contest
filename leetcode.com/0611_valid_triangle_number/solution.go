func triangleNumber(nums []int) int {
    total := 0
    sort.Ints(nums[:])

    for i := 0 ; i < len(nums) ; i++ {
        for j := i + 1 ; j < len(nums) ; j++ {
            for k := j + 1 ; k < len(nums) ; k++ {
                a, b, c := nums[i], nums[j], nums[k]
                if a + b > c && a + c > b && b + c > a {
                    total++
                } else {
                    break
                }
            }
        }
    }

    return total

}
