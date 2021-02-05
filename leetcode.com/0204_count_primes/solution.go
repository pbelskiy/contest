package main

import "fmt"

var non_prime[5000000] bool

func countPrimes(n int) int {
    if (n < 2) {
        return 0
    }

    if non_prime[3] == false {
        for i := 2; i < len(non_prime); i++ {
            for j := i * i; j < len(non_prime); j += i {
                non_prime[j - 1] = true;
            }
        }
    }

    count := 0

    for i := 1; i < len(non_prime); i++ {
        if (non_prime[i - 1] == false) {
            if (i >= n) {
                return count - 1
            }

            count++
        }
    }

    return count
}

func main() {
    fmt.Printf("%d == 0\n", countPrimes(0))
    fmt.Printf("%d == 0\n", countPrimes(1))
    fmt.Printf("%d == 0\n", countPrimes(2))
    fmt.Printf("%d == 4\n", countPrimes(10))

    fmt.Printf("%d == 41537\n", countPrimes(499979))
    fmt.Printf("%d == 41537\n", countPrimes(499979))
}
