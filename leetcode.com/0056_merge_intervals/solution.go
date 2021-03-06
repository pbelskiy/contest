import "sort"

func merge(intervals [][]int) [][]int {
    var merged[][]int

    sort.SliceStable(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    merged = append(merged, intervals[0])

    for i := 1 ; i < len(intervals) ; i++ {
        if merged[len(merged) - 1][1] < intervals[i][0] {    
            merged = append(merged, intervals[i])
            continue
        }

        if merged[len(merged) - 1][1] < intervals[i][1] {
            merged[len(merged) - 1][1] = intervals[i][1]   
        }
    }

    return merged
}


