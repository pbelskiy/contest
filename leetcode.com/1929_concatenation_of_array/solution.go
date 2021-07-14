func getConcatenation(nums []int) []int {
    array := make([]int, len(nums)*2)

    for i := 0 ; i < len(nums) ; i++ {
        array[i] = nums[i]
        array[len(nums) + i] = nums[i]
    }

    return array
}
