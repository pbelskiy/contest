package main

import "fmt"
import "math"

func updateMatrix(matrix [][]int) [][]int {
    out_matrix := make([][]int, len(matrix))
    for x := 0; x < len(matrix); x++ {
        out_matrix[x] = make([]int, len(matrix[x]))

        for y := 0; y < len(matrix[x]); y++ {
            if matrix[x][y] == 0 {
                out_matrix[x][y] = 0
            } else {
                out_matrix[x][y] = math.MaxInt32
            }
        }
    }

    for true {
        solved := 0
        for x := 0; x < len(out_matrix); x++ {
            for y := 0; y < len(out_matrix[x]); y++ {
                if out_matrix[x][y] == 0 {
                    continue
                }

                if x-1 >= 0 && out_matrix[x-1][y] + 1 < out_matrix[x][y] {
                    out_matrix[x][y] = out_matrix[x-1][y] + 1
                    solved++
                }

                if y-1 >= 0 && out_matrix[x][y-1]+1 < out_matrix[x][y] {
                    out_matrix[x][y] = out_matrix[x][y-1]+1
                    solved++
                }

                if x+1 < len(out_matrix) && out_matrix[x+1][y]+1 < out_matrix[x][y] {
                    out_matrix[x][y] = out_matrix[x+1][y]+1
                    solved++
                }

                if y+1 < len(out_matrix[x]) && out_matrix[x][y+1]+1 < out_matrix[x][y] {
                    out_matrix[x][y] = out_matrix[x][y+1]+1
                    solved++
                }
            }
        }

        if (solved == 0) {
            break
        }
    }

    return out_matrix
}

func main() {
    matrix := [][]int{
        {1, 1, 0, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 0, 1, 1, 1, 1, 1, 1, 1},
        {1, 1, 1, 1, 0, 0, 0, 1, 1, 0},
        {1, 1, 1, 1, 1, 1, 0, 0, 1, 0},
        {1, 0, 0, 1, 1, 1, 0, 1, 0, 1},
        {0, 0, 1, 0, 0, 1, 1, 0, 0, 1},
        {0, 1, 0, 1, 1, 1, 1, 1, 1, 1},
        {1, 0, 0, 1, 1, 0, 0, 0, 0, 0},
        {0, 0, 1, 1, 1, 1, 0, 1, 1, 1},
        {1, 1, 0, 0, 1, 0, 1, 0, 1, 1},
    }

    new_matrix := updateMatrix(matrix)

    fmt.Println("\nnew matrix:")
    for x := 0; x < len(new_matrix); x++ {
        for y := 0; y < len(new_matrix[x]); y++ {
            fmt.Printf("%d ", new_matrix[x][y])
        }
        fmt.Println()
    }
}
