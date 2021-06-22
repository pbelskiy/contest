func replaceDigits(s string) string {
    b := []byte(s)

    for i := 1 ; i < len(b) ; i += 2 {
        b[i] = b[i-1] + b[i] - '0'
    }

    return string(b)
}
