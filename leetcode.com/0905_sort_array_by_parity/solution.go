package main

import "fmt"

func sortArrayByParity(A []int) []int {
    var sorted = make([]int, len(A))
    var begin int
    var end int

    for _, value := range A {
        if value % 2 == 0 && end <= begin {
            sorted[end] = value
            end++;
            begin++
        } else if value % 2 != 0 {
            sorted[end] = value
            end++
        } else {
            tmp := sorted[begin]
            sorted[begin] = value
            sorted[end] = tmp
            begin++
            end++
        }
    }

    return sorted
}

func main() {
    fmt.Println(sortArrayByParity([]int{0,1,2}))
}
