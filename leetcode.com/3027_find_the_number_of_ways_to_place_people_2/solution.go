func numberOfPairs(points [][]int) int {
    t := 0
    for _, p1 := range points {
        x1, y1 := p1[0], p1[1]
        for _, p2 := range points {
            x2, y2 := p2[0], p2[1]
            if x1 == x2 && y1 == y2 {
                continue
            }

            if !(x2 >= x1 && y2 <= y1) {
                continue
            }
            inside := 0
            for _, p := range points {
                x, y := p[0], p[1]
                if (x == x1 && y == y1) || (x == x2 && y == y2) {
                    continue
                }
                if x >= x1 && x <= x2 && y >= y2 && y <= y1 {
                    inside++
                    break
                }
            }
            if inside == 0 {
                t++
            }
        }
    }
    return t
}
