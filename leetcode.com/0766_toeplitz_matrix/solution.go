package main

import "fmt"

func check(matrix [][]int, y, x int) bool {
    target := matrix[y][x]

    for ; y < len(matrix) && x < len(matrix[0]); y, x = y+1, x+1 {
        if matrix[y][x] != target {
            return false
        }
    }

    return true
}

func isToeplitzMatrix(matrix [][]int) bool {

    for y := len(matrix) - 1 ; y >= 0 ; y-- {
        if (!check(matrix, y, 0)) {
            return false
        }
    }

    for x := 1 ; x < len(matrix[0]) ; x++ {
        if (!check(matrix, 0, x)) {
            return false
        }
    }

    return true
}

func main() {
    matrix := [][]int{{1,2,3,4},{5,1,2,3},{9,5,1,2}}
    fmt.Println(isToeplitzMatrix(matrix))
}
