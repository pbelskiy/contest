package main

import (
	"fmt"
	"math"
)

func minSideJumps(obstacles []int) int {
	cache := make(map[[3]int]int)
	var dp func(int, int, bool) int
	dp = func(i, p int, j bool) int {
		if i == len(obstacles)-1 {
			return 0
		}
		if val, ok := cache[[3]int{i, p, boolToInt(j)}]; ok {
			return val
		}
		m := math.MaxInt32
		if i+1 < len(obstacles) && obstacles[i+1] != p {
			m = min(m, dp(i+1, p, false))
		}
		for _, np := range []int{p - 1, p - 2, p + 1, p + 2} {
			if !j && 1 <= np && np <= 3 && obstacles[i] != np {
				m = min(m, dp(i, np, true)+1)
			}
		}
		cache[[3]int{i, p, boolToInt(j)}] = m
		return m
	}
	return dp(0, 2, false)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func boolToInt(b bool) int {
	if b {
		return 1
	}
	return 0
}
