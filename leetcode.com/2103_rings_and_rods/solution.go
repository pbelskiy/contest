func countPoints(rings string) int {
    rods := make(map[byte]int)

    for i := 0 ; i < len(rings) - 1 ; i += 2 {
        if rings[i] == 'R' {
            rods[rings[i + 1]] |= 1 << 0
            continue
        }

        if rings[i] == 'G' {
            rods[rings[i + 1]] |= 1 << 1
            continue
        }

        if rings[i] == 'B' {
            rods[rings[i + 1]] |= 1 << 2
            continue
        }
    }

    total := 0

    for k := range rods {
        if rods[k] == 1 | 2 | 4 {
            total += 1
        }
    }

    return total
}
