func containsNearbyDuplicate(nums []int, k int) bool {
    h := make(map[int]int)

    for i, n := range(nums) {

        if v, ok := h[n]; ok {
            if i - v <= k {
                return true
            }
        }

        h[n] = i
    }

    return false
}
