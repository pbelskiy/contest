func isOneBitCharacter(bits []int) bool {
    found := false
    
    for i := 0 ; i < len(bits) ; i++ {
        if bits[i] == 1 {
            i += 1
        } else if (i + 1 == len(bits)) {
            found = true
        }
    }
    
    return found
}


