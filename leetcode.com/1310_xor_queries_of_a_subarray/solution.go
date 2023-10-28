import "fmt"

func xorQueries(arr []int, queries [][]int) []int {
    res := []int{}

    for i := 0 ; i < len(queries) ; i++ {
        v := 0

        for j := queries[i][0] ; j <= queries[i][1] ; j++ {
            v ^= arr[j]
        }

        res = append(res, v)
    }

    return res
}
