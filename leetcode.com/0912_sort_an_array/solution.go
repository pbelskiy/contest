func quicksort(nums []int, l, r int) {
    if l >= r {
        return
    }

    val := nums[(l + r) / 2]

    i := l
    j := r

    for i <= j {
        for ; nums[i] < val ; i++ {}
        for ; nums[j] > val ; j-- {}

        if i >= j {
            break
        }

        nums[i], nums[j] = nums[j], nums[i]
        i++
        j--
    }

    quicksort(nums, l, j)
    quicksort(nums, j + 1, r)
}

func sortArray(nums []int) []int {
    quicksort(nums, 0, len(nums) - 1)
    return nums
}
