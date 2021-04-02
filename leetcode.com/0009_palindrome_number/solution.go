import "strconv"

func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }

    s := strconv.Itoa(x)
    r := []rune(s)

    for i := 0 ; i < len(s) / 2 ; i++ {
        if r[i] != r[len(s) - 1 - i] {
            return false
        }
    }

    return true
}
