package main

import "fmt"
import "strconv"

func solve(s string, pos int, sum int) (int, int) {
    add := true

    for i := pos ; i < len(s) ; i++ {
        switch (s[i]) {
        case ' ':
            continue

        case '-':
            add = false
            continue

        case '+':
            add = true
            continue

        case '(':
            new_pos, new_sum := solve(s, i + 1, 0)

            if (add) {
                sum += new_sum
            } else {
                sum -= new_sum
            }

            i = new_pos
            continue

        case ')':
            return i, sum

        default:
            l := 0

            for i + l < len(s) {
                if (s[i + l] == ' ' || s[i + l] == '+' || s[i + l] == '-' ||
                    s[i + l] == '(' || s[i + l] == ')') {
                        break
                    }

                    l++
            }

            val, _ := strconv.Atoi(string(s[i:i+l]))
            i += l - 1

            if (add) {
                sum += val
            } else {
                sum -= val
            }
        }
    }

    return pos, sum
}

func calculate(s string) int {
    _, sum := solve(s, 0, 0)
    return sum
}

func main() {
    // fmt.Printf("%d == 2\n", calculate("1 + 1"))
    // fmt.Printf("%d == 4\n", calculate("3-(4-5)"))
    // fmt.Printf("%d == -6\n", calculate("(0-(6))"))
    // fmt.Printf("%d == -1\n", calculate("(9-10)"))
    fmt.Printf("%d == 23\n", calculate("(1+(4+5+2)-3)+(6+8)"))
}
