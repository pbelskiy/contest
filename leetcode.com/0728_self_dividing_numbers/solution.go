func selfDividingNumbers(left int, right int) []int {
    list := make([]int, 0, right - left + 1)

    for n := left ; n <= right ; n++ {

        x := n
        ok := true

        for x > 0 {
            ln := x % 10

            if ln == 0 {
                ok = false
                break
            }

            if n % ln != 0 {
                ok = false
                break
            }

            x /= 10
        }

        if (ok) {
            list = append(list, n)
        }
    }

    return list
}