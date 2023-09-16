func countPairs(coordinates [][]int, k int) int {
	t := 0
	for i := 0; i < len(coordinates); i++ {
		for j := i + 1; j < len(coordinates); j++ {
            if ((coordinates[i][0] ^ coordinates[j][0]) + (coordinates[i][1] ^ coordinates[j][1])) == k {
				t += 1
			}
		}
	}
	return t
}
