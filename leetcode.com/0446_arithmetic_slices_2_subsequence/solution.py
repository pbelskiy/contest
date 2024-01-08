var cache = make(map[[3]int]int)

func dfs(i int, j int, d int, nums []int) int {
    if i == len(nums) {
        return 0
    }

    if val, ok := cache[[3]int{i, j, d}]; ok {
        return val
    }

    t := 0
    for k := i; k < len(nums); k++ {
        if j == -1000000000 {
            t += dfs(k+1, k, -1000000000, nums)
        } else if d == -1000000000 {
            t += dfs(k+1, k, nums[k]-nums[j], nums)
        } else if nums[j]+d == nums[k] {
            t += dfs(k+1, k, d, nums) + 1
        }
    }

    cache[[3]int{i, j, d}] = t
    return t
}

func numberOfArithmeticSlices(nums []int) int {
    clear(cache)
    return dfs(0, -1000000000, -1000000000, nums)
}
