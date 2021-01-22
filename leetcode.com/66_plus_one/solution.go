package main

import "fmt"

func plusOne(digits []int) []int {

    for i := len(digits) - 1 ; i >= 0 ; i-- {
        fmt.Println(i, digits[i])

        if digits[i] + 1 <= 9 {
            digits[i]++
            break
        }

        digits[i] = 0

        if i == 0 {
            digits = append([]int{1}, digits...)
        }
    }

    return digits
}

func main() {
    fmt.Println(plusOne([]int{9,9}))
}
