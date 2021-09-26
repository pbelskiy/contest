func finalValueAfterOperations(operations []string) int {
    x := 0

    for _, op := range operations {
        if strings.Contains(op, "-") {
            x--
        } else {
            x++
        }
    }

    return x
}