package main

import "fmt"
import "math"

var values [10000]int

func min(a, b int) int {
    if (a < b) {
        return a
    }

    return b
}

func numSquares(n int) int {
    if values[1] != 0 {
        return values[n]
    }

    for v := 1 ; v < len(values) ; v++ {
        ps := int(math.Floor(math.Sqrt(float64(v))))
        delta := v - ps*ps

        if delta == 0 {
            values[v] = 1
        } else {
            values[v] = values[ps*ps] + values[delta]

            for s := ps - 1 ; s > 0 ; s-- {
                delta := v - s*s
                values[v] = min(values[v], values[s*s] + values[delta])
            }
        }
    }

    return values[n]
}

func main() {
    fmt.Println(numSquares(12))
}
