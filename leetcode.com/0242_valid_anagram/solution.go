func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    letters := map[rune]int{}
    
    for _, l := range s {
        letters[l]++
    }
    
    for _, l := range t {
        letters[l]--
    }
    
    for _, v := range letters {
        if v != 0 {
            return false
        }
    }
    
    return true
}
